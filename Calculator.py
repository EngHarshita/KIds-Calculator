import os
import speech_recognition as sr
from gtts import gTTS

# Initialize recognizer object
recognizer = sr.Recognizer()

# Function to convert text to speech
def text_to_speech(text):
    # Convert text to speech
    speech = gTTS(text=text, lang='en')
    speech.save("output.mp3")
    os.system("mpg321 output.mp3")

# Function to calculate expression
def calculate(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "Invalid expression"

# Main function
def main():
    print("Welcome to the Kids Calculator!")
    print("You can input your expression in both written and voice format.")

    while True:
        print("\nEnter your expression (or type 'exit' to quit):")
        user_input = input()

        if user_input.lower() == 'exit':
            break

        # If the input is a written expression
        if user_input.strip():
            result = calculate(user_input)
            print("Result:", result)
            text_to_speech("The result is " + str(result))
        
        # If the input is a voice command
        else:
            print("Please speak your expression:")
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
            try:
                voice_input = recognizer.recognize_google(audio)
                result = calculate(voice_input)
                text_to_speech("You said: " + voice_input)
                text_to_speech("The result is " + str(result))
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that.")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    main()