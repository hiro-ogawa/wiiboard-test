import struct

import pyaudio
from blessed import Terminal

RATE = 44100
CHUNK = 512

class VCO():
    def __init__(self):
        self.m = 0
        self.data = [0] * CHUNK #初期化

    def square(self,freq=220,amp=0.1):
        t0 = int(RATE / freq)
        for n in range(CHUNK):
            if(self.m >= t0/2):
                sign = 1
            else:
                sign = -1
            s = amp * sign
            self.m += 1
            if(self.m >= t0):
                self.m = 0
            self.data[n] = int(s * 32767.0)
        data_out = self.data
        return data_out

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    t = Terminal()

    stream = p.open(format=pyaudio.paInt16,channels=1, rate=44100, output=1)
    m = 0 #初期値
    note_num = 60
    vco = VCO()
    with t.cbreak():
        while True:
            k = t.inkey(timeout=0.000001)
            if(k.name == 'KEY_ESCAPE'):
                break
            if(str.isdigit(k)):
                note_num = int(k) + 60
            concert_pitch = 440
            freq = concert_pitch * (2**((note_num-69)/12)) 
            print(freq, k, end="\r")
            data = vco.square(freq = freq, amp = 0.1)
            data = struct.pack("h" * len(data), *data) #バイナリ変換
            stream.write(data)