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

bt = 2.0 #half notes/rest
bt_long = bt + 0.5
bt_eight = bt/2 #eight notes/rest
bt_sixt = bt_eight/2 #sixteent notes/ rest

vol = 1.0
sin_sig = []
def createNote(noteName = "A4", type = "sine", amp = 0.5, beats = 1.0, filter = None, cutoff = None, filename = "default") :
    frequency  = noteFreqs[noteName]
    duration = beats/2

    for i in range (0,8):
        
        sin_sig = thinkdsp.SinSignal(freq=frequency*i, amp=amp*fourier_coeffs[type][i], offset=0) 

    
    wave = sin_sig.make_wave(duration = duration, start = 0 , framerate = 44100)
    print(wave)
    wave.write(filename=filename)
    audio = AudioSegment.from_wav(filename)
#filter
    return audio 
A1 = createNote(noteName = "A1", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
C1 = createNote(noteName = "C1", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
E1 = createNote(noteName = "E1", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
F1 = createNote(noteName = "F1", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
G1 = createNote(noteName = "G1", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
D1 = createNote(noteName = "D1", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
Gb1 = createNote(noteName = "Gb1", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
B1 = createNote(noteName = "B1", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
C2 = createNote(noteName = "C2", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
D2 = createNote(noteName = "C2", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)

Eb1 = createNote(noteName = "Eb1", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
Ab1 = createNote(noteName = "Ab1", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
rest = createNote(noteName = "rest", type = "random", amp = vol, beats = bt, filter = None, cutoff = None)
rest_eight = createNote(noteName = "rest", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)

A1_eight = createNote(noteName = "A1", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
C1_eight = createNote(noteName = "C1", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
E1_eight = createNote(noteName = "E1", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
F1_eight = createNote(noteName = "F1", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
G1_eight = createNote(noteName = "G1", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
D1_eight = createNote(noteName = "D1", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
Gb1_eight = createNote(noteName = "Gb1", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
B1_eight = createNote(noteName = "B1", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
C2_eight = createNote(noteName = "C2", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
D2_eight = createNote(noteName = "D2", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
G2_eight = createNote(noteName = "G2", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
G3_eight = createNote(noteName = "G3", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)
Eb1_eight = createNote(noteName = "G3", type = "random", amp = vol, beats = bt_eight, filter = None, cutoff = None)

A1_sixt = createNote(noteName = "A1", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
C1_sixt = createNote(noteName = "C1", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
E1_sixt = createNote(noteName = "E1", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
F1_sixt = createNote(noteName = "F1", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
G1_sixt = createNote(noteName = "G1", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
D1_sixt = createNote(noteName = "D1", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
Gb1_sixt = createNote(noteName = "Gb1", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
B1_sixt = createNote(noteName = "B1", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
C2_sixt = createNote(noteName = "C2", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
D2_sixt = createNote(noteName = "D2", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
G2_sixt = createNote(noteName = "G2", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
G3_sixt = createNote(noteName = "G3", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)
Eb1_sixt = createNote(noteName = "G3", type = "random", amp = vol, beats = bt_sixt, filter = None, cutoff = None)


A1_long = createNote(noteName = "A1", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
C1_long = createNote(noteName = "C1", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
E1_long = createNote(noteName = "E1", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
F1_long = createNote(noteName = "F1", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
G1_long = createNote(noteName = "G1", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
D1_long = createNote(noteName = "D1", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
Gb1_long = createNote(noteName = "Gb1", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
B1_long = createNote(noteName = "B1", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
C2_long = createNote(noteName = "C2", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
D2_long = createNote(noteName = "D2", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
G2_long = createNote(noteName = "G2", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
G3_long = createNote(noteName = "G3", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)
Eb1_long = createNote(noteName = "G3", type = "random", amp = vol, beats = bt_long, filter = None, cutoff = None)