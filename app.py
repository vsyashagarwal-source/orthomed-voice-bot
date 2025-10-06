from flask import Flask, request
from twilio.twiml import VoiceResponse
import json
import re

app = Flask(__name__)

class OrthoMedicalBot:
    def __init__(self):
        self.medical_kb = {
            "arthritis": {
                "symptoms": ["joint pain", "stiffness", "swelling", "reduced range of motion"],
                "info": "Arthritis is inflammation of joints. Common types include osteoarthritis and rheumatoid arthritis.",
                "advice": "Apply ice or heat, gentle exercise, maintain healthy weight. See orthopedic specialist for proper diagnosis."
            },
            "back_pain": {
                "symptoms": ["lower back pain", "back pain", "muscle spasms", "stiffness", "radiating pain"],
                "info": "Back pain can result from muscle strain, herniated discs, or spinal conditions.",
                "advice": "Rest, gentle stretching, proper posture. Seek immediate care if numbness or severe pain occurs."
            },
            "fracture": {
                "symptoms": ["severe pain", "swelling", "deformity", "inability to move", "broken bone"],
                "info": "Bone fractures require immediate medical attention for proper healing.",
                "advice": "Immobilize the area, apply ice, seek emergency care immediately."
            },
            "knee_pain": {
                "symptoms": ["knee pain", "swelling", "clicking sounds", "instability"],
                "info": "Knee pain can be from ligament injuries, meniscus tears, or arthritis.",
                "advice": "RICE protocol - Rest, Ice, Compression, Elevation. See orthopedic specialist."
            },
            "shoulder_pain": {
                "symptoms": ["shoulder pain", "limited movement", "weakness", "catching sensation"],
                "info": "Common causes include rotator cuff injuries, frozen shoulder, or impingement.",
                "advice": "Avoid overhead activities, gentle range of motion exercises, consult specialist."
            }
        }
    
    def emergency_detection(self, text):
        emergency_keywords = [
            "severe pain", "can't move", "open wound", "bone sticking out",
            "numbness", "tingling", "loss of feeling", "emergency",
            "accident", "fell", "broken bone visible", "bleeding"
        ]
        
        text_lower = text.lower()
        for keyword in emergency_keywords:
            if keyword in text_lower:
                return True
        return False
    
    def analyze_symptoms(self, user_input):
        user_input_lower = user_input.lower()
        matched_conditions = []
        
        for condition, data in self.medical_kb.items():
            for symptom in data["symptoms"]:
                if symptom.lower() in user_input_lower:
                    matched_conditions.append(condition)
                    break
        
        return matched_conditions
    
    def generate_response(self, user_input):
        disclaimer = "Please note: I provide educational information only and cannot replace professional medical diagnosis. "
        
        if self.emergency_detection(user_input):
            return disclaimer + "This sounds like it could be an emergency situation. Please call 911 or go to your nearest emergency room immediately."
        
        conditions = self.analyze_symptoms(user_input)
        
        if not conditions:
            return disclaimer + "I'd be happy to help with information about orthopedic conditions. Could you describe your symptoms more specifically? For example, are you experiencing joint pain, back pain, or injury-related concerns?"
        
        response = disclaimer
        for condition in conditions[:2]:
            data = self.medical_kb[condition]
            response += f"Regarding {condition.replace('_', ' ')}: {data['info']} "
            response += f"General advice: {data['advice']} "
        
        response += "I strongly recommend consulting with a qualified orthopedic specialist for proper evaluation and treatment."
        return response

bot = OrthoMedicalBot()

@app.route("/", methods=['GET'])
def home():
    return """
    <h1>OrthoMed Voice Bot</h1>
    <p>Orthopedic Medical Assistant - AI-powered voice bot for orthopedic consultations</p>
    <p>Call the Twilio number to interact with the bot</p>
    """

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    
    response.say("""Hello! I'm your Orthopedic Medical Assistant. 
    I provide educational information about bone, joint, and musculoskeletal conditions. 
    Please note that I provide general information only and cannot replace professional medical diagnosis.
    Please describe your symptoms or concerns after the beep.""", voice='alice')
    
    gather = response.gather(input='speech', timeout=10, action='/process', speechTimeout='auto')
    gather.say("Please speak now.")
    
    response.say("I didn't hear anything. Please call back if you need assistance.")
    
    return str(response)

@app.route("/process", methods=['POST'])
def process():
    user_speech = request.form.get('SpeechResult', '')
    
    if not user_speech:
        response = VoiceResponse()
        response.say("I didn't catch that. Could you please repeat your question?")
        response.redirect('/voice')
        return str(response)
    
    bot_response = bot.generate_response(user_speech)
    
    response = VoiceResponse()
    response.say(bot_response, voice='alice')
    
    gather = response.gather(input='speech', timeout=8, action='/process', speechTimeout='auto')
    gather.say("Do you have any other questions? Please speak after the beep, or hang up if you're done.")
    
    response.say("Thank you for using OrthoMed Assistant. Remember to consult with a healthcare professional for any medical concerns. Goodbye!")
    
    return str(response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)