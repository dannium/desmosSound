import wave
import struct
import numpy as np
import matplotlib.pyplot as plt

#returns first half of list
def half(list):
    return list[:len(list)//2]

print("go to https://www.desmos.com/calculator/yccglkqkej to get the template\n\n")

#change "theaudio.wav" to any .wav file to read (has to be in the same directory as this script)
with wave.open("theaudio.wav", "rb") as audio:
    print("Converting data...")
    frameRate = audio.getframerate() #amount of frames per second
    frameCount = audio.getnframes() #number of frames total
    channelCount = audio.getnchannels() #mono (same in both ears) or 2 channels
    isByte = audio.getsampwidth() == 1 #tells whether data stored as 1 or 2 bytes

    #probably too much converting but whatever
    binaryData = audio.readframes(frameCount) 
    data = struct.unpack("<" + ("b" if(isByte) else "h")*channelCount*frameCount, binaryData) #unpacks data to tuple
    data = str(data) #converts to string
    data = data[1:len(data)-1] #removes first and last chars (parentheses)
    data = data.split(", ") #converts to list
    for i in range(len(data)):
        data[i] = int(data[i]) #converts all items of list to ints

    #average out audio channels if left/right ear seperate
    if(channelCount == 2):
        tempData = data
        for i in range(len(data)//2):
            data[i] = (tempData[i*2] + tempData[i*2 + 1])//2
        data = data[:len(data)//2]
    


    ######################################## convert with fourier
    desmosData = []

    fps = frameRate//int(input("How many frames do you want to play in desmos each second? (Recommended ~10)\n"))
    totalFrames = len(data)//fps


    layerNum = int(input("How many layers do you want? (Recommended ~150 for short (5s), ~40 for long (30s+))\n"))

    for i in range(layerNum):
        desmosData.append("b_{" + str(i) + "} = [")

    print("formatting data to desmos...")
    for frameNum in range(totalFrames):
        dataChunk = data[frameNum*fps:(frameNum+1)*fps]  
        #freqs (x)
        freqs = half(np.fft.fftfreq(len(dataChunk), d=1/frameRate))
        #amp of freqs (y)
        amps = half(abs(np.fft.fft(dataChunk)))

        freqs = freqs[10:]
        amps = amps[10:]

        #get top (layerNum) loudest frequencies in frame
        sortedAmps = sorted(enumerate(amps/frameRate*16/100), key=lambda x: x[1], reverse=True)[:layerNum]
        for i in range(layerNum):
            #(desmosData[0] = loudest frequency of each frame, desmosData[1] = 2nd loudest, etc)
            desmosData[i] += f"({int(freqs[sortedAmps[i][0]])}, {sortedAmps[i][1]/10:.5f}), "

            f"{i:.5f}" 
    
    print("\n"*10)
    print("Copy paste into desmos under data folder: \n")

    for i in range(layerNum):
        desmosData[i] = desmosData[i][:-2] + "]"
        print(desmosData[i])
    
    print("\n(Scroll all the way up)\n")
    input("press enter once you've pasted into desmos ")

    print("\n"*10)
    print("Copy paste these under the play folder in desmos to actually play the song: \n")
    for i in range(layerNum):
        print("f(b_{" + str(i) + "})")

    print("\n(Scroll up a bit)")


    '''
    #graph frame
    plt.plot(freqs, amps, color="blue")
    plt.ylabel("ts amplitudes")
    plt.xlabel("ts frequencies")
    plt.title("test")
    plt.show()'''