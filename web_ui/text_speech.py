import pyttsx3

engine = pyttsx3.init()

while True:
    # answer = input("Enter the sentence you want to spell")
    answer = "namaste aap kaise hain"
    engine.say(answer)
    engine.runAndWait()
