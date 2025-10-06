#!/usr/bin/env python3
"""
Automated setup script for OrthoMed Voice Bot
This script will automatically:
1. Deploy the application
2. Set up Twilio integration
3. Make test calls
"""

import os
import requests
import json
from twilio.rest import Client
import time

class AutoSetup:
    def __init__(self):
        self.app_url = None
        self.twilio_client = None
        self.phone_number = None
        
    def check_deployment_status(self):
        """Check if the app is deployed and running"""
        possible_urls = [
            "https://orthomed-voice-bot-latest.onrender.com",
            "https://orthomed-voice-bot.onrender.com",
            "https://orthomed-voice-bot-production.up.railway.app"
        ]
        
        for url in possible_urls:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    self.app_url = url
                    print(f"✅ App deployed successfully at: {url}")
                    return True
            except:
                continue
                
        print("❌ App not yet deployed. Please deploy first.")
        return False
    
    def setup_twilio(self, account_sid=None, auth_token=None):
        """Set up Twilio client and phone number"""
        
        # Use environment variables or provided credentials
        if not account_sid:
            account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        if not auth_token:
            auth_token = os.getenv('TWILIO_AUTH_TOKEN')
            
        if not account_sid or not auth_token:
            print("⚠️  Twilio credentials not provided.")
            print("Please set TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN environment variables")
            print("Or get them from: https://console.twilio.com/")
            return False
            
        try:
            self.twilio_client = Client(account_sid, auth_token)
            
            # Get available phone numbers
            phone_numbers = self.twilio_client.incoming_phone_numbers.list(limit=1)
            
            if phone_numbers:
                self.phone_number = phone_numbers[0].phone_number
                print(f"✅ Using existing phone number: {self.phone_number}")
                
                # Update webhook URL
                phone_numbers[0].update(
                    voice_url=f"{self.app_url}/voice",
                    voice_method='POST'
                )
                print(f"✅ Webhook configured: {self.app_url}/voice")
                return True
            else:
                print("❌ No phone numbers found. Please buy a Twilio number first.")
                return False
                
        except Exception as e:
            print(f"❌ Twilio setup failed: {str(e)}")
            return False
    
    def make_test_call(self, to_number):
        """Make a test call to verify the bot works"""
        
        if not self.twilio_client or not self.phone_number:
            print("❌ Twilio not set up properly")
            return False
            
        try:
            call = self.twilio_client.calls.create(
                to=to_number,
                from_=self.phone_number,
                url=f"{self.app_url}/voice",
                method='POST'
            )
            
            print(f"✅ Test call initiated!")
            print(f"📞 Call SID: {call.sid}")
            print(f"📱 Calling: {to_number}")
            print(f"🤖 Bot will provide orthopedic consultation")
            
            return call.sid
            
        except Exception as e:
            print(f"❌ Test call failed: {str(e)}")
            return False
    
    def run_full_setup(self, target_number="+918081345736"):
        """Run the complete automated setup"""
        
        print("🚀 Starting automated OrthoMed Voice Bot setup...")
        print("=" * 50)
        
        # Step 1: Check deployment
        print("1️⃣ Checking deployment status...")
        if not self.check_deployment_status():
            print("Please deploy the app first using:")
            print("- Railway: https://railway.app/new/template/orthomed-voice-bot")
            print("- Render: https://render.com/deploy")
            return False
        
        # Step 2: Setup Twilio
        print("\n2️⃣ Setting up Twilio integration...")
        if not self.setup_twilio():
            return False
        
        # Step 3: Test the system
        print(f"\n3️⃣ Making test call to {target_number}...")
        call_sid = self.make_test_call(target_number)
        
        if call_sid:
            print("\n🎉 SETUP COMPLETE!")
            print("=" * 50)
            print(f"🌐 App URL: {self.app_url}")
            print(f"📞 Phone Number: {self.phone_number}")
            print(f"🤖 Bot Status: Active")
            print(f"📱 Test Call: {call_sid}")
            
            print("\n📋 What happens next:")
            print("1. The bot will call +918081345736")
            print("2. Answer the call to hear the welcome message")
            print("3. Describe orthopedic symptoms")
            print("4. Bot provides medical information")
            
            print("\n🧪 Test phrases to try:")
            print("- 'I have knee pain and swelling'")
            print("- 'My back hurts when I bend'")
            print("- 'Joint stiffness in the morning'")
            print("- 'Severe pain, can't move' (emergency test)")
            
            return True
        else:
            print("❌ Setup incomplete. Check Twilio configuration.")
            return False

if __name__ == "__main__":
    setup = AutoSetup()
    
    # Run automated setup
    success = setup.run_full_setup()
    
    if success:
        print("\n✅ OrthoMed Voice Bot is now live and ready!")
        print("📞 Call the Twilio number to test the orthopedic consultation bot")
    else:
        print("\n❌ Setup failed. Please check the configuration and try again.")
        
    print("\n🔗 Useful links:")
    print("- GitHub Repo: https://github.com/vsyashagarwal-source/orthomed-voice-bot")
    print("- Twilio Console: https://console.twilio.com/")
    print("- Deploy to Railway: https://railway.app/")
    print("- Deploy to Render: https://render.com/")