# Desmos Audio
converts data from .wav files into desmos

## About 
ok so I’m sure you’ve seen people make a bunch of stuff on Desmos, bad apple, minecraft, but somehow playing audio was like the one thing that hadn’t been done (from what I saw), so I decided to make desmos audio

All it is is a single python script. desmos only allows you to make sound by choosing frequencies to play instead of how .wav files work with holding the actual air pressure data. I could’ve used mp3s, since they were in the same format as desmos uses with frequencies, but I didn’t feel like learning how to decompress all the data, so I just went with wavs.

It works by using the Fourier Transform every fraction of a second to find the loudest frequencies and their volumes (I don’t actually know how the Fourier transform works, I’m still a junior lol, I just imported using numpy). Desmos freaks out if you have more than like 500 frequencies (most sounds have thousands) so I had to only play the loudest frequencies to make it work, although this means it isn’t as accurate.

I made the script easy for users so that you can customize the quality settings and the audio that is being played. I also made a template at https://www.desmos.com/calculator/yccglkqkej to make it easier too

## Running
To run the script, download the project, or just the python file (wavToDesmos.py), and open it in whatever IDE you use (I used Visual Studio 2026)
