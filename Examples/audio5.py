import struct
import wave

w = wave.open('music.wav', 'wb')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)

frequency = 440  # Hz
waveforms = frequency // 4
width = 44100 // frequency // 2
volume = 4000

for i in range(waveforms):
    amplitude = volume - volume * i // waveforms
    for j in range(width):
        w.writeframes(struct.pack('<h', amplitude))
    for j in range(width):
        w.writeframes(struct.pack('<h', -amplitude))
