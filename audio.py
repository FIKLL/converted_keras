import speech_recognition as sr

# Create an instance of the Recognizer class
recognizer = sr.Recognizer()

# Create audio file instance from the original file
audio_ex = sr.AudioFile('Recording (8).wav')
type(audio_ex)

# Create audio data
with audio_ex as source:
    audiodata = recognizer.record(audio_ex)
type(audiodata)

# Extract text
text = recognizer.recognize_google(audio_data=audiodata, language='fr-FR')
#untuk indo pake 'id-ID'
#untuk france pake 'fr-FR'

print(text)