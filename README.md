# 🏥 OrthoMed Voice Bot

AI-powered orthopedic medical assistant that provides educational information about bone, joint, and musculoskeletal conditions via phone calls.

## 🚀 One-Click Deployment

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/github.com/vsyashagarwal-source/orthomed-voice-bot)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/vsyashagarwal-source/orthomed-voice-bot)

## ⚡ Automated Setup

After deployment, run the automated setup:

```bash
python auto_setup.py
```

This will automatically:
- ✅ Verify deployment status
- ✅ Configure Twilio webhook
- ✅ Make test call to +918081345736
- ✅ Verify bot functionality

## 🩺 Medical Features

### Supported Conditions
- **Arthritis** (osteoarthritis, rheumatoid)
- **Back Pain** (herniated discs, muscle strain)
- **Fractures** (bone injuries, emergency detection)
- **Knee Problems** (ligament injuries, sports injuries)
- **Shoulder Issues** (rotator cuff, frozen shoulder)

### Safety Features
- 🚨 **Emergency Detection** → Immediate 911 referral
- ⚠️ **Medical Disclaimers** on every response
- 👨‍⚕️ **Professional Referrals** for proper diagnosis
- 🔒 **Scope Limitations** clearly defined

## 📞 Call Flow

```
📱 Incoming Call
    ↓
🤖 "Hello! I'm your Orthopedic Medical Assistant..."
    ↓
🗣️ User describes symptoms
    ↓
🧠 AI analyzes condition
    ↓
📋 Provides educational information
    ↓
👨‍⚕️ Recommends specialist consultation
```

## 🧪 Test Scenarios

Try these phrases when calling:

| Input | Expected Response |
|-------|------------------|
| "I have knee pain" | Knee injury information + RICE protocol |
| "My back hurts" | Back pain causes + posture advice |
| "Joint stiffness" | Arthritis information + exercise tips |
| "Severe pain, can't move" | Emergency → "Call 911 immediately" |
| "Shoulder weakness" | Rotator cuff info + specialist referral |

## 🛠️ Technical Stack

- **Backend**: Flask + Python
- **Voice**: Twilio Voice API
- **Speech**: Google Speech Recognition
- **AI**: Custom medical knowledge base
- **Deployment**: Railway/Render (free tiers)

## 📋 Manual Setup (if needed)

### 1. Deploy Application
```bash
# Option A: Railway
git clone https://github.com/vsyashagarwal-source/orthomed-voice-bot
cd orthomed-voice-bot
# Deploy to Railway

# Option B: Render
# Connect GitHub repo to Render
```

### 2. Twilio Configuration
```bash
# Get Twilio credentials from console.twilio.com
# Buy phone number ($1/month)
# Set webhook: https://your-app.railway.app/voice
```

### 3. Test Call
```bash
# Call your Twilio number
# Or run: python test_call.py
```

## 🔧 Environment Variables

```bash
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
PORT=8080  # Auto-set by hosting platforms
```

## 📊 Bot Capabilities

### ✅ What the Bot CAN Do:
- Provide educational information about orthopedic conditions
- Explain common symptoms and causes
- Suggest general self-care measures
- Detect emergency situations
- Recommend when to seek professional help
- Guide users through basic symptom assessment

### ❌ What the Bot CANNOT Do:
- Diagnose specific medical conditions
- Prescribe medications or treatments
- Replace professional medical consultation
- Provide personalized medical advice
- Handle complex medical emergencies (redirects to 911)

## 🚨 Important Medical Disclaimer

**This bot provides educational information only and cannot replace professional medical diagnosis or treatment. Always consult with a qualified orthopedic specialist for proper evaluation and treatment of medical conditions.**

## 📞 Live Demo

Once deployed, your bot will be available at:
- **Phone**: Your Twilio number
- **Web**: https://your-app.railway.app
- **Test Call**: Automatically calls +918081345736

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Add medical conditions or improve responses
4. Test with voice calls
5. Submit pull request

## 📄 License

MIT License - Feel free to use for educational and medical information purposes.

---

**🏥 Built for better healthcare accessibility through AI voice technology**