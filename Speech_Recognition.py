import speech_recognition as sr # type: ignore
import wave
from playsound import playsound # type: ignore

# Initialize recognizer class
r = sr.Recognizer()

# Set the filename for temporary audio storage
audio_file = "recorded_audio.wav"

# Record from microphone
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")

# Save the recorded audio to a WAV file
with open(audio_file, "wb") as f:
    f.write(audio_text.get_wav_data())

# Play back the recorded audio
print("Playing recorded audio...")
playsound(audio_file)

# Recognize the speech in the audio
try:
    # Using Google Speech Recognition
    print("Text: " + r.recognize_google(audio_text))
except sr.UnknownValueError:
    print("Sorry, I did not get that")
except sr.RequestError:
    print("Could not request results from Google Speech Recognition service")
