import wave
import struct

with wave.open("theaudio.wav", "rb") as audio:
    frameRate = audio.getframerate() #amount of frames per second
    frameCount = audio.getnframes() #number of frames total
    channelCount = audio.getnchannels() #mono (same in both ears) or 2 channels
    isByte = audio.getsampwidth() == 1 #tells whether data stored as 1 or 2 bytes

    #probably too much converting but whatever
    binaryData = audio.readframes(frameCount) 
    data = struct.unpack("<" + ("b" if(isByte) else "h")*channelCount*frameCount, binaryData) #unpacks data to tuple
    data = str(data) #converts to string
    data = (data[:len(data)-1])[1:] #removes first and last chars (parentheses)
    data = data.split(", ") #converts to list
    for i in range(len(data)):
        data[i] = int(data[i]) #converts all items of list to ints

