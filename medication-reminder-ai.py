#!/usr/bin/env python3
"""
import numpy as np
from sklearn.naive_bayes import BernoulliNB
import random
import sys

# Optional: Try to import OpenCV, but don't fail if not available
try:
import cv2
OPENCV_AVAILABLE = True
except ImportError:
OPENCV_AVAILABLE = False
print("Note: OpenCV not available. Using simulated computer vision instead.")

class MedicationReminderAI:
def __init__(self):
self.medications_database = [
{'name': 'Lisinopril', 'frequency': 'Daily', 'priority': 1, 'type': 'Blood Pressure'},
{'name': 'Metformin', 'frequency': 'Morning and Evening', 'priority': 1, 'type': 'Diabetes'},
{'name': 'Aspirin', 'frequency': 'Daily', 'priority': 2, 'type': 'Heart Health'},
{'name': 'Vitamin D', 'frequency': 'Daily', 'priority': 3, 'type': 'Supplement'}
]

# Initialize Naive Bayes model for adherence risk
self.adherence_model = self._train_adherence_model()

def _train_adherence_model(self):
"""Train Naive Bayes classifier for medication adherence risk assessment"""
# Training data: [missed_morning, missed_evening, forgot_multiple_days, side_effects]
X = np.array([
[0, 0, 0, 0], # Perfect adherence
[1, 0, 0, 0], # Missed morning only
[0, 1, 0, 0], # Missed evening only
[1, 1, 0, 0], # Missed both doses one day
[0, 0, 1, 0], # Forgot multiple days
[1, 1, 1, 0], # Multiple issues
[0, 0, 0, 1], # Side effects only
[1, 1, 1, 1], # All risk factors
[1, 0, 1, 0], # Missed morning + multiple days
[0, 1, 1, 1], # Multiple risk factors
])

# Labels: 0 = Low risk, 1 = High risk
y = np.array([0, 0, 0, 0, 1, 1, 0, 1, 1, 1])

model = BernoulliNB(alpha=1.0) # Laplacian smoothing
model.fit(X, y)
return model

def recognize_medication_label(self, image_path=None):
"""Simulated computer vision for medication label recognition"""
print("\n🔍 Analyzing medication label...")

# Simulate processing time
import time
time.sleep(1)

# Simulate different medication recognition results
simulated_medications = [
"Medication: Lisinopril 10mg\nInstructions: Take once daily\nRefills: 2 remaining",
"Medication: Metformin 500mg\nInstructions: Take twice daily with meals\nRefills: 1 remaining",
"Medication: Aspirin 81mg\nInstructions: Take once daily\nRefills: 3 remaining"
]

recognized_text = random.choice(simulated_medications)
print("✅ Label Recognition Complete!")
return recognized_text

def chatbot_interface(self):
"""Interactive chatbot for medication queries"""
print("\n" + "="*50)
print("👋 Hello! I'm your AI Medication Assistant.")
print("I can help you with:")
print(" • Medication reminders ('reminder')")
print(" • Side effect information ('side effects')")
print(" • Drug interactions ('interactions')")
print(" • Risk assessment ('risk')")
print(" • General medication questions")
print("="*50)

while True:
try:
user_input = input("\n💬 How can I help you today? (or 'exit' to quit): ").lower().strip()

if user_input == 'exit' or user_input == 'quit':
print("👋 Goodbye! Remember to take your medications on time. Stay healthy!")
break

elif user_input == 'reminder':
self.run_reminder_system()

elif 'side effect' in user_input:
self.provide_side_effect_info()

elif 'interaction' in user_input:
self.provide_interaction_info()

elif user_input == 'risk':
self.assess_adherence_risk()

elif 'help' in user_input:
self.show_help()

elif user_input == '':
continue

else:
self.handle_general_query(user_input)

except KeyboardInterrupt:
print("\n👋 Goodbye! Stay healthy!")
break
except Exception as e:
print(f"❌ Sorry, I encountered an error: {e}")
print("Please try again or type 'help' for assistance.")

def run_reminder_system(self):
"""Rule-based expert system for medication scheduling"""
print("\n📋 MEDICATION REMINDER SYSTEM")
print("-" * 40)

# Expert system rules: Sort by priority and type
high_priority_meds = [med for med in self.medications_database if med['priority'] == 1]
medium_priority_meds = [med for med in self.medications_database if med['priority'] == 2]
low_priority_meds = [med for med in self.medications_database if med['priority'] == 3]

print("🔴 HIGH PRIORITY (Critical Medications):")
for med in high_priority_meds:
print(f" ✅ {med['name']} - {med['frequency']} ({med['type']})")

print("\n🟡 MEDIUM PRIORITY:")
for med in medium_priority_meds:
print(f" ✅ {med['name']} - {med['frequency']} ({med['type']})")

print("\n🟢 LOW PRIORITY (Supplements):")
for med in low_priority_meds:
print(f" ✅ {med['name']} - {med['frequency']} ({med['type']})")

print("\n🎯 Expert System Recommendation:")
print(" • Take high-priority medications first")
print(" • Set alarms for twice-daily medications")
print(" • Take with food if stomach-sensitive")
print(" • Never skip critical heart/diabetes medications")

def assess_adherence_risk(self):
"""Use Naive Bayes to assess medication adherence risk"""
print("\n🔍 MEDICATION ADHERENCE RISK ASSESSMENT")
print("-" * 45)

try:
# Collect user data
print("Please answer the following questions (1=yes, 0=no):")

missed_morning = self._get_binary_input("Did you miss your morning dose today? ")
missed_evening = self._get_binary_input("Did you miss your evening dose today? ")
forgot_multiple = self._get_binary_input("Have you forgotten medications for multiple days? ")
side_effects = self._get_binary_input("Are you experiencing side effects? ")

# Make prediction
user_data = [[missed_morning, missed_evening, forgot_multiple, side_effects]]
prediction = self.adherence_model.predict(user_data)
probabilities = self.adherence_model.predict_proba(user_data)[0]

# Display results
risk_level = "HIGH RISK" if prediction[0] == 1 else "LOW RISK"
confidence = max(probabilities) * 100

print(f"\n📊 RISK ASSESSMENT RESULTS:")
print(f" Risk Level: {risk_level}")
print(f" Confidence: {confidence:.1f}%")
print(f" Low Risk Probability: {probabilities[0]:.3f}")
print(f" High Risk Probability: {probabilities[1]:.3f}")

# Provide recommendations
if prediction[0] == 1:
print("\n⚠️ RECOMMENDATIONS:")
print(" • Set multiple daily alarms")
print(" • Use a pill organizer")
print(" • Ask family member to check in")
print(" • Consult your doctor about side effects")
else:
print("\n✅ Great job maintaining medication adherence!")
print(" • Continue your current routine")
print(" • Keep tracking your progress")

except Exception as e:
print(f"❌ Error during risk assessment: {e}")

def _get_binary_input(self, prompt):
"""Helper function to get binary (0/1) input from user"""
while True:
try:
value = input(prompt + "(1=yes, 0=no): ").strip()
if value in ['0', '1']:
return int(value)
else:
print(" Please enter only 0 or 1.")
except KeyboardInterrupt:
raise
except:
print(" Please enter only 0 or 1.")

def provide_side_effect_info(self):
"""Provide information about common medication side effects"""
side_effects_db = {
'lisinopril': 'Common: dry cough, dizziness, headache. Serious: swelling, difficulty breathing.',
'metformin': 'Common: nausea, diarrhea, stomach upset. Take with food to reduce symptoms.',
'aspirin': 'Common: stomach irritation, heartburn. Serious: unusual bleeding, ringing in ears.',
'general': 'Always report unusual symptoms to your doctor immediately.'
}

print("\n💊 MEDICATION SIDE EFFECTS INFORMATION:")
for med, effects in side_effects_db.items():
if med != 'general':
print(f" {med.title()}: {effects}")
print(f" ⚠️ {side_effects_db['general']}")

def provide_interaction_info(self):
"""Provide drug interaction warnings"""
print("\n⚠️ DRUG INTERACTION WARNINGS:")
print(" • Avoid grapefruit with heart medications")
print(" • Don't mix aspirin with blood thinners")
print(" • Alcohol can increase side effects")
print(" • Always tell doctors about ALL medications")
print(" • Check with pharmacist before adding supplements")

def show_help(self):
"""Display help information"""
print("\n📖 HELP - Available Commands:")
print(" 'reminder' - Get medication schedule")
print(" 'risk' - Assess adherence risk")
print(" 'side effects' - Learn about side effects")
print(" 'interactions' - Drug interaction warnings")
print(" 'help' - Show this help message")
print(" 'exit' - Quit the program")

def handle_general_query(self, query):
"""Handle general medication questions"""
responses = [
"🤖 For specific medical advice, please consult your doctor or pharmacist.",
"💊 I can help with reminders, side effects, and general medication information.",
"🏥 If you have urgent concerns, contact your healthcare provider immediately.",
"📱 Try asking about 'reminders', 'side effects', or 'interactions'."
]
print(random.choice(responses))

def main():
"""Main function to run the Medication Reminder AI System"""
print("🏥 MEDICATION REMINDER AI SYSTEM")
print("=" * 50)
print("AI Techniques Used:")
print(" • Computer Vision (Simulated)")
print(" • Expert Systems (Rule-based)")
print(" • Naive Bayes Classification")
print(" • Natural Language Processing")
print("=" * 50)

# Initialize the AI system
ai_system = MedicationReminderAI()

try:
# Demonstrate computer vision capability
print("\n📸 MEDICATION LABEL RECOGNITION:")
label_info = ai_system.recognize_medication_label()
print(label_info)

# Start interactive chatbot
ai_system.chatbot_interface()

except KeyboardInterrupt:
print("\n\n👋 Program interrupted. Goodbye!")
except Exception as e:
print(f"\n❌ An error occurred: {e}")
print("Please restart the program.")

if __name__ == "__main__":
main()
