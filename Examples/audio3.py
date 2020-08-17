import struct
import wave

w = wave.open('music.wav', 'wb')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)

waveforms = 5000
width = 4
volume = 4000

for i in range(waveforms):
    for j in range(width):
        w.writeframes(struct.pack('<h', volume))

    for j in range(width):
        w.writeframes(struct.pack('<h', -volume))
