import wave

with wave.open("theaudio.wav", "rb") as audio:
    print(audio.getframerate())