# medication_reminder_ai.py

import cv2
import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn.preprocessing import LabelBinarizer
import random

# Simulated prescription label recognition function
def recognize_medication_label(image_path):
    # For demonstration, return simulated medication data
    recognized_text = "Medication: Lisinopril\nDosage: 10mg\nFrequency: Daily"
    return recognized_text

# Chatbot interface for elderly users
def chatbot_interface():
    print("\n👋 Hello! I'm your medication assistant.")
    while True:
        user_input = input("💬 Ask me anything or type 'reminder' to start reminders (or 'exit' to quit): ").lower()
        if user_input == 'exit':
            print("👋 Goodbye! Stay healthy.")
            break
        elif user_input == 'reminder':
            run_reminder_system()
        elif 'side effect' in user_input:
            print("💊 Common side effects: dizziness, cough, headache.")
        elif 'interaction' in user_input:
            print("💊 Avoid grapefruit juice with this medication. Check with your doctor!")
        else:
            print("🤖 I'm here to help! Ask about dosage, interactions, or side effects.")

# Simulated medication reminder planner (symbolic planning)
def run_reminder_system():
    medications = [
        {'name': 'Lisinopril', 'frequency': 'Daily', 'priority': 2},
        {'name': 'Metformin', 'frequency': 'Morning and Evening', 'priority': 1},
        {'name': 'Aspirin', 'frequency': 'Daily', 'priority': 3}
    ]

    # Rule-based expert system: Prioritize high-risk medication reminders
    sorted_meds = sorted(medications, key=lambda m: m['priority'])

    print("\n🔔 Medication Reminder Schedule:")
    for med in sorted_meds:
        print(f"✅ Take {med['name']} ({med['frequency']})")

    print("👍 Stay on schedule to stay healthy!\n")

# Naive Bayes classifier for adherence risk
def adherence_risk_classifier():
    # Simulated dataset: 1 = missed dose, 0 = took dose
    # Features: [Missed morning, Missed evening]
    X = np.array([
        [0, 0],
        [1, 0],
        [0, 1],
        [1, 1],
        [1, 1]
    ])
    # Labels: 0 = Low risk, 1 = High risk
    y = np.array([0, 0, 0, 1, 1])

    model = BernoulliNB(alpha=1.0)  # Laplacian correction
    model.fit(X, y)

    # Simulated user input
    missed_morning = int(input("Did you miss your morning dose? (1=yes, 0=no): "))
    missed_evening = int(input("Did you miss your evening dose? (1=yes, 0=no): "))

    prediction = model.predict([[missed_morning, missed_evening]])
    proba = model.predict_proba([[missed_morning, missed_evening]])

    risk_label = "High risk" if prediction[0] == 1 else "Low risk"
    print(f"\n🔍 Your adherence risk level: {risk_label}")
    print(f"📊 Probability: {proba}")

# Main driver
def main():
    print("📸 Simulated Medication Label Recognition")
    label_info = recognize_medication_label("medication_label.jpg")
    print(label_info)

    chatbot_interface()
    adherence_risk_classifier()

if __name__ == "__main__":
    main()
