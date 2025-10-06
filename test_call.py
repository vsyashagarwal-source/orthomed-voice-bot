#!/usr/bin/env python3
"""
Test script to make outbound calls using Twilio
Replace with your Twilio credentials
"""

from twilio.rest import Client

# Twilio credentials (replace with your actual values)
TWILIO_ACCOUNT_SID = 'your_account_sid_here'
TWILIO_AUTH_TOKEN = 'your_auth_token_here'
TWILIO_PHONE_NUMBER = 'your_twilio_number_here'  # Format: +1234567890

def make_test_call(to_number):
    """Make a test call to the specified number"""
    
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    try:
        call = client.calls.create(
            to=to_number,
            from_=TWILIO_PHONE_NUMBER,
            url='https://your-app-url.onrender.com/voice',  # Replace with your actual URL
            method='POST'
        )
        
        print(f"✅ Call initiated successfully!")
        print(f"📞 Call SID: {call.sid}")
        print(f"📱 To: {to_number}")
        print(f"🤖 Bot will answer and provide orthopedic consultation")
        
        return call.sid
        
    except Exception as e:
        print(f"❌ Error making call: {str(e)}")
        return None

if __name__ == "__main__":
    # Test call to the specified number
    target_number = "+918081345736"
    
    print("🚀 Making test call to orthopedic bot...")
    print(f"📞 Calling: {target_number}")
    
    call_sid = make_test_call(target_number)
    
    if call_sid:
        print("\n🎯 Test Call Instructions:")
        print("1. Answer the call")
        print("2. Listen to the bot's welcome message")
        print("3. Describe orthopedic symptoms (e.g., 'I have knee pain')")
        print("4. Bot will provide medical information")
        print("5. Ask follow-up questions or hang up")
        
        print("\n🧪 Test Scenarios:")
        print("- 'I have back pain' → Back pain information")
        print("- 'My knee is swollen' → Knee injury advice")
        print("- 'Severe pain, can't move' → Emergency response")
        print("- 'Joint stiffness' → Arthritis information")
    else:
        print("❌ Call failed. Check your Twilio credentials and try again.")