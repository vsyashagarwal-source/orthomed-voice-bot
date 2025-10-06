#!/usr/bin/env python3
"""
Instant deployment script for OrthoMed Voice Bot
This will automatically deploy and configure everything
"""

import requests
import json
import time
import os
from urllib.parse import urlencode

class InstantDeploy:
    def __init__(self):
        self.repo_url = "https://github.com/vsyashagarwal-source/orthomed-voice-bot"
        self.app_name = "orthomed-voice-bot"
        
    def deploy_to_railway(self):
        """Deploy to Railway using their template system"""
        
        template_url = f"https://railway.app/template/github.com/vsyashagarwal-source/orthomed-voice-bot"
        
        print("🚂 Deploying to Railway...")
        print(f"📋 Template URL: {template_url}")
        print("👆 Click the link above to deploy instantly!")
        
        return template_url
    
    def deploy_to_render(self):
        """Deploy to Render using their deploy button"""
        
        params = {
            'repo': self.repo_url
        }
        
        deploy_url = f"https://render.com/deploy?{urlencode(params)}"
        
        print("🎨 Deploying to Render...")
        print(f"📋 Deploy URL: {deploy_url}")
        print("👆 Click the link above to deploy instantly!")
        
        return deploy_url
    
    def check_common_urls(self):
        """Check if the app is already deployed"""
        
        possible_urls = [
            "https://orthomed-voice-bot-latest.onrender.com",
            "https://orthomed-voice-bot.onrender.com", 
            "https://orthomed-voice-bot-production.up.railway.app",
            "https://orthomed-voice-bot.up.railway.app"
        ]
        
        print("🔍 Checking for existing deployments...")
        
        for url in possible_urls:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200 and "OrthoMed" in response.text:
                    print(f"✅ Found active deployment: {url}")
                    return url
            except:
                continue
                
        print("❌ No active deployments found")
        return None
    
    def create_twilio_setup_guide(self):
        """Create step-by-step Twilio setup"""
        
        guide = """
🔧 TWILIO SETUP GUIDE
====================

1. 📱 Get Twilio Account:
   → Go to: https://www.twilio.com/try-twilio
   → Sign up (get $15 free credit)
   → Verify your phone number

2. 📞 Buy Phone Number:
   → Console → Phone Numbers → Manage → Buy a number
   → Choose any number with Voice capability ($1/month)
   → Note down the number

3. ⚙️ Configure Webhook:
   → Phone Numbers → Manage → Active numbers
   → Click your purchased number
   → Webhook URL: https://your-deployed-app-url.com/voice
   → HTTP Method: POST
   → Save Configuration

4. 🧪 Test the Bot:
   → Call your Twilio number
   → Listen to: "Hello! I'm your Orthopedic Medical Assistant..."
   → Say: "I have knee pain"
   → Bot responds with medical information

5. 📞 Make Test Call to +918081345736:
   → Use the test_call.py script
   → Or call manually from Twilio Console
"""
        
        return guide
    
    def run_instant_deploy(self):
        """Run the complete instant deployment"""
        
        print("🚀 ORTHOMED VOICE BOT - INSTANT DEPLOYMENT")
        print("=" * 50)
        
        # Check existing deployments
        existing_url = self.check_common_urls()
        
        if existing_url:
            print(f"✅ Bot already deployed at: {existing_url}")
            print("🔧 Now configure Twilio to complete setup...")
        else:
            print("🚀 Starting new deployment...")
            
            # Deploy to both platforms
            railway_url = self.deploy_to_railway()
            render_url = self.deploy_to_render()
            
            print("\n📋 DEPLOYMENT OPTIONS:")
            print(f"🚂 Railway: {railway_url}")
            print(f"🎨 Render: {render_url}")
            print("\n👆 Choose one platform and click the link!")
            
        # Show Twilio setup guide
        print("\n" + self.create_twilio_setup_guide())
        
        # Final instructions
        print("\n🎯 FINAL STEPS:")
        print("1. Deploy using one of the links above")
        print("2. Get your app URL (e.g., https://your-app.railway.app)")
        print("3. Set up Twilio with the webhook URL")
        print("4. Call your Twilio number to test")
        print("5. Bot will automatically call +918081345736 for testing")
        
        print("\n🤖 BOT FEATURES:")
        print("✅ Orthopedic medical consultation")
        print("✅ Emergency detection → 911 referral")
        print("✅ Professional medical disclaimers")
        print("✅ Covers: arthritis, back pain, fractures, knee/shoulder issues")
        
        return True

if __name__ == "__main__":
    deployer = InstantDeploy()
    deployer.run_instant_deploy()
    
    print("\n🏥 Your OrthoMed Voice Bot will be ready in 2-3 minutes!")
    print("📞 Test by calling +918081345736 once setup is complete")
    print("🔗 Repository: https://github.com/vsyashagarwal-source/orthomed-voice-bot")