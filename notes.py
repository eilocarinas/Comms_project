import thinkdsp
import random
from pydub import AudioSegment
from pydub.playback import play
from thinkdsp import SinSignal

noteFreqs = {
    'C0':16.35, 'Db0':17.32,'D0':18.35,'Eb0':19.45,'E0':20.6,'F0':21.83,'Gb0':23.12,\
    'G0':24.5,'Ab0':25.96,'A0':27.5,'Bb0':29.14,'B0':30.87,'C1':32.7,'Db1':34.65,'D1':36.71,\
    'Eb1':38.89,'E1':41.2,'F1':43.65,'Gb1':46.25,'G1':49,'Ab1':51.91,'A1':55,'Bb1':58.27,\
    'B1':61.74,'C2':65.41,'Db2':69.3,'D2':73.42,'Eb2':77.78,'E2':82.41,'F2':87.31,'Gb2':92.5,\
    'G2':98,'Ab2':103.83,'A2':110,'Bb2':116.54,'B2':123.47,'C3':130.81,'Db3':138.59,'D3':146.83,\
    'Eb3':155.56,'E3':164.81,'F3':174.61,'Gb3':185,'G3':196,'Ab3':207.65,'A3':220,'Bb3':233.08,\
    'B3':246.94,'C4':261.63,'Db4':277.18,'D4':293.66,'Eb4':311.13,'E4':329.63,'F4':349.23,\
    'Gb4':369.99,'G4':392,'Ab4':415.3,'A4':440,'Bb4':466.16,'B4':493.88,'C5':523.25,'Db5':554.37,\
    'D5':587.33,'Eb5':622.25,'E5':659.25,'F5':698.46,'Gb5':739.99,'G5':783.99,'Ab5':830.61,'A5':880,\
    'Bb5':932.33,'B5':987.77,'C6':1046.5,'Db6':1108.73,'D6':1174.66,'Eb6':1244.51,'E6':1318.51,\
    'F6':1396.91,'Gb6':1479.98,'G6':1567.98,'Ab6':1661.22,'A6':1760,'Bb6':1864.66,'B6':1975.53,\
    'C7':2093,'Db7':2217.46,'D7':2349.32,'Eb7':2489.02,'E7':2637.02,'F7':2793.83,'Gb7':2959.96,\
    'G7':3135.96,'Ab7':3322.44,'A7':3520,'Bb7':3729.31,'B7':3951.07,'C8':4186.01,'Db':4434.92,\
    'D8':4698.63,'Eb8':4978.03,'E8':5274.04,'F8':5587.65,'Gb8':5919.91,'G8':6271.93,'Ab8':6644.88,\
    'A8':7040,'Bb8':7458.62,'B8':7902.13, 'rest':0

}

random_coeffs = []
for i in range (0, 8):
    random_coeffs.append(random.uniform(-1, 1))

fourier_coeffs = {
    "sine": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "trumpet": [0.1155, 0.3417, 0.1789, 0.1232, 0.0678, 0.0473, 0.0260, 0.0045, 0.0020],
    "random": random_coeffs 
}

bt = 1.5 #half notes/rest

bt_eight = bt/2 #eight notes/rest
bt_sixt = bt_eight/2 #sixteenth      notes/ rest

bt_long = bt*2
vol = 1.0
low_vol = vol/2
sin_sig = []
def createNote(noteName = "A4", type = "sine", amp = 0.5, beats = 1.0, filter = None, cutoff = None, filename = "default") :
    frequency  = noteFreqs[noteName]
    duration = beats/2
    sin_sig = thinkdsp.SinSignal(freq=0)
   # sin_sig = thinkdsp.SinSignal(freq=frequency, amp=amp, offset=0) 
    for i in range(0, 8):  # delete if not fourier
        sin_sig += thinkdsp.SinSignal(freq=frequency*i, amp=amp*fourier_coeffs[type][i], offset=0) 
    wave = sin_sig.make_wave(duration = duration, start = 0 , framerate = 44100)
    print(wave)
    wave.write(filename=filename)
    audio = AudioSegment.from_wav(filename)
    # filter
    audio = audio.low_pass_filter(440)
#filter
    return audio 

A3 = createNote(noteName = "A3", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)
C3 = createNote(noteName = "C3", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)
E3 = createNote(noteName = "E3", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)
F3 = createNote(noteName = "F3", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)
G3 = createNote(noteName = "G3", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)
D3 = createNote(noteName = "D3", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)
Gb3 = createNote(noteName = "Gb3", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)
B3 = createNote(noteName = "B3", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)
C2 = createNote(noteName = "C2", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)
D2 = createNote(noteName = "C2", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)
E2 = createNote(noteName = "E2", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)
Eb3 = createNote(noteName = "Eb3", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)
Ab3 = createNote(noteName = "Ab3", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)
rest = createNote(noteName = "rest", type = "random", amp = low_vol, beats = bt, filter = None, cutoff = None)


A3_eight = createNote(noteName = "A3", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
C3_eight = createNote(noteName = "C3", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
E3_eight = createNote(noteName = "E3", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
F3_eight = createNote(noteName = "F3", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
G3_eight = createNote(noteName = "G3", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
D3_eight = createNote(noteName = "D3", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
Gb3_eight = createNote(noteName = "Gb3", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
B3_eight = createNote(noteName = "B3", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
C2_eight = createNote(noteName = "C2", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
D2_eight = createNote(noteName = "D2", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
G2_eight = createNote(noteName = "G2", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
G3_eight = createNote(noteName = "G3", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
Eb3_eight = createNote(noteName = "G3", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
E2_eight = createNote(noteName = "E2", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)
rest_eight = createNote(noteName = "rest", type = "random", amp = low_vol, beats = bt_eight, filter = None, cutoff = None)


A3_sixth = createNote(noteName = "A3", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
C3_sixth = createNote(noteName = "C3", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
E3_sixth = createNote(noteName = "E3", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
F3_sixth = createNote(noteName = "F3", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
G3_sixth = createNote(noteName = "G3", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
D3_sixth = createNote(noteName = "D3", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
Gb3_sixth = createNote(noteName = "Gb3", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
B3_sixth = createNote(noteName = "B3", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
C2_sixth = createNote(noteName = "C2", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
D2_sixth = createNote(noteName = "D2", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
G2_sixth = createNote(noteName = "G2", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
G3_sixth = createNote(noteName = "G3", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
Eb3_sixth = createNote(noteName = "G3", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
E2_sixth = createNote(noteName = "E2", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)
rest_sixth = createNote(noteName = "rest", type = "random", amp = low_vol, beats = bt_sixt, filter = None, cutoff = None)


D3 = createNote(noteName="D3", type="random", amp=low_vol, beats=bt, filter=None, cutoff=None)

A3_long = createNote(noteName = "A3", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)
C3_long = createNote(noteName = "C3", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)
E3_long = createNote(noteName = "E3", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)
F3_long = createNote(noteName = "F3", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)
G3_long = createNote(noteName = "G3", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)
D3_long = createNote(noteName = "D3", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)
Gb3_long = createNote(noteName = "Gb3", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)
B3_long = createNote(noteName = "B3", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)
C2_long = createNote(noteName = "C2", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)
D2_long = createNote(noteName = "D2", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)
G2_long = createNote(noteName = "G2", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)
G3_long = createNote(noteName = "G3", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)
Eb3_long = createNote(noteName = "G3", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)
E2_long = createNote(noteName = "E2", type = "random", amp = low_vol, beats = bt_long, filter = None, cutoff = None)

A4 = createNote(noteName = "A4", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
C4 = createNote(noteName = "C4", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
E4 = createNote(noteName = "E4", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
F4 = createNote(noteName = "F4", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
G4 = createNote(noteName = "G4", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
D4 = createNote(noteName = "D4", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
Gb4 = createNote(noteName = "Gb4", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
B4 = createNote(noteName = "B4", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
C5 = createNote(noteName = "C5", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
D5 = createNote(noteName = "C5", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
E5 = createNote(noteName = "E5", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
Eb4 = createNote(noteName = "Eb4", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
Ab4 = createNote(noteName = "Ab4", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
rest = createNote(noteName = "rest", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)


A4_eight = createNote(noteName = "A4", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
C4_eight = createNote(noteName = "C4", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
E4_eight = createNote(noteName = "E4", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
F4_eight = createNote(noteName = "F4", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
G4_eight = createNote(noteName = "G4", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
D4_eight = createNote(noteName = "D4", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
Gb4_eight = createNote(noteName = "Gb4", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
B4_eight = createNote(noteName = "B4", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
C5_eight = createNote(noteName = "C5", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
D5_eight = createNote(noteName = "D5", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
G5_eight = createNote(noteName = "G5", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
G3_eight = createNote(noteName = "G3", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
Eb4_eight = createNote(noteName = "G3", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
E5_eight = createNote(noteName = "E5", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
rest_eight = createNote(noteName = "rest", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)


A4_sixth = createNote(noteName = "A4", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
C4_sixth = createNote(noteName = "C4", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
E4_sixth = createNote(noteName = "E4", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
F4_sixth = createNote(noteName = "F4", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
G4_sixth = createNote(noteName = "G4", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
D4_sixth = createNote(noteName = "D4", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
Gb4_sixth = createNote(noteName = "Gb4", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
B4_sixth = createNote(noteName = "B4", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
C5_sixth = createNote(noteName = "C5", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
D5_sixth = createNote(noteName = "D5", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
G5_sixth = createNote(noteName = "G5", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
G3_sixth = createNote(noteName = "G3", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
Eb4_sixth = createNote(noteName = "G3", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
E5_sixth = createNote(noteName = "E5", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
rest_sixth = createNote(noteName = "rest", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)


D3 = createNote(noteName="D3", type="random", amp=vol, beats=bt, filter=None, cutoff=None)

A4_long = createNote(noteName = "A4", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
C4_long = createNote(noteName = "C4", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
E4_long = createNote(noteName = "E4", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
F4_long = createNote(noteName = "F4", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
G4_long = createNote(noteName = "G4", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
D4_long = createNote(noteName = "D4", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
Gb4_long = createNote(noteName = "Gb4", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
B4_long = createNote(noteName = "B4", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
C5_long = createNote(noteName = "C5", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
D5_long = createNote(noteName = "D5", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
G5_long = createNote(noteName = "G5", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
G3_long = createNote(noteName = "G3", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
Eb4_long = createNote(noteName = "G3", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
E5_long = createNote(noteName = "E5", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)

D6 = createNote(noteName="D6", type="random", amp=vol, beats=bt, filter=None, cutoff=None)
