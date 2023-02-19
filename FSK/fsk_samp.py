import thinkdsp
import random
from pydub import AudioSegment
from pydub.playback import play


seg_track1 = []
seg_track2 = [] 
two_bit = []

bt = 1.5

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
# 00-sixteenth  01- eighth  10-quarter 11-half

part1_message = "10010110100101010101100101100101101001010101001001"
part1_message_long = "11111111111111111111111111111111111111111111111111"
part2_message = "10011010011001100110011001100111100110100110011001100110011001100111"
part2_message_long = "11111111111111111111111111111111111111111111111111111111111111111111"
part3_message = "01010110101010010101011001010110101001011010"
part3_message_long = "11111111111111111111111111111111111111111111"

part1_note = ['G4', 'Gb4', 'A4', 'G4',   # Ba-yang Ma-gi-
                'D4', 'A4', 'B4', 'C5',    # -liw per-las ng
                'B4', 'A4', 'B4', 'G4', 'rest',  # si-la-nga-nan
                'G4', 'Gb4', 'A4', 'G4',   # a-lab-ng-pu-
                'D4', 'A4', 'B4', 'C5',    # so sa dib-dib
                'B4', 'A4', 'G4', 'rest'    # mo'y bu-hay
                ]

part1_note_f = ['G4', 'Gb4', 'A4', 'G4',   # Ba-yang Ma-gi-
                'D4', 'A4', 'B4', 'C5',    # -liw per-las ng
                'B4', 'A4', 'B4', 'G4', 'rest',  # si-la-nga-nan
                'G4', 'Gb4', 'A4', 'G4',   # a-lab-ng-pu-
                'D4', 'A4', 'B4', 'C5',    # so sa dib-dib
                'B4', 'A4', 'G4', 'rest'    # mo'y bu-hay
                ]

part1_note = [ 'G4', 'Gb4', 'A4', 'G4',   # Lu-pang hi-ni
               'D4', 'A4', 'B4', 'C5',    # rang du-yan ka
               'B4', 'A4', 'B4', 'G4', 'rest',  # ng ma-gi-ting
               'G4', 'Gb4', 'A4', 'G4',   # sa man-lu-lu
               'D4', 'A4', 'B4', 'C5',     # pig 'di ka pa-
               'B4', 'A4', 'G4', 'rest'   # si-si-il
              ]

part1_note_f = [ 'G4', 'Gb4', 'A4', 'G4',   # Lu-pang hi-ni
                 'D4', 'A4', 'B4', 'C5',    # rang du-yan ka
                 'B4', 'A4', 'B4', 'G4', 'rest',  # ng ma-gi-ting
                 'G4', 'Gb4', 'A4', 'G4',   # sa man-lu-lu
                 'D4', 'A4', 'B4', 'C5',    # pig 'di ka pa-
                 'B4', 'A4', 'G4', 'rest'   # si-si-il
                ]


part2_note = [ 'G4','Gb4', 'G4','A4','A4','D4','D4',  # Ang kis-lap ng wa-ta-wat
                'A4','A4','D4','D4',                  # mo'y ta-gum-pay
                'B4', 'C5', 'D5', 'E5','D5',          # na nag-ni-ning-ning
                'G4','Gb4', 'G4','A4','A4','D4','D4', # Ang bi-tu-in at a-raw
                'A4','A4','D4','D4',                  # niya ka-i-lan
                'B4','C5','B4','A4','B4','A4','G4'    # pa ma'y 'di mag-di-di-lim
               ]

part2_note_f = [ 'G4','Gb4', 'G4','A4','A4','D4','D4',  # Ang kis-lap ng wa-ta-wat
                'A4','A4','D4','D4',                  # mo'y ta-gum-pay
                'B4', 'C5', 'D5', 'E5','D5',          # na nag-ni-ning-ning
                'G4','Gb4', 'G4','A4','A4','D4','D4', # Ang bi-tu-in at a-raw
                'A4','A4','D4','D4',                  # niya ka-i-lan
                'B4','C5','B4','A4','B4','A4','G4'    # pa ma'y 'di mag-di-di-lim
               ]

part3_note = ['G4', 'E4', 'G4', 'C4',         # Lu-pa ng a-
              'C4', 'D4', 'D4', 'E4',         # raw ng luwal-ha-
              'D4', 'C4', 'D4', 'E4',         # ti't pag-si-nta
              'Gb4', 'E4', 'D4', 'E4',        # Bu-hay ay la
              'C4', 'D4', 'B4', 'B4', 'C4', 'rest'  # ngit sa pi-ling mo
              ]

part3_note_f = ['G4', 'E4', 'G4', 'C4',         # Lu-pa ng a-
              'C4', 'D4', 'D4', 'E4',         # raw ng luwal-ha-
              'D4', 'C4', 'D4', 'E4',         # ti't pag-si-nta
              'Gb4', 'E4', 'D4', 'E4',        # Bu-hay ay la
              'C4', 'D4', 'B4', 'B4', 'C4', 'rest'  # ngit sa pi-ling mo
              ]

part3_note = ['G4', 'E4', 'G4', 'C4',         # A-ming li-ga
              'C4', 'D4', 'D4', 'E4',         # ya na 'pag may
              'D4', 'C4', 'D4', 'E4',         # mang-a-a-pi
              'Gb4', 'E4', 'D4', 'E4',        # Ang ma-ma-tay
              'C4', 'D4', 'B4', 'B4', 'C4', 'rest'  # nang da-hil sa-'yo
              ]

part3_note_f = ['G4', 'E4', 'G4', 'C4',         # A-ming li-ga
              'C4', 'D4', 'D4', 'E4',         # ya na 'pag may
              'D4', 'C4', 'D4', 'E4',         # mang-a-a-pi
              'Gb4', 'E4', 'D4', 'E4',        # Ang ma-ma-tay
              'C4', 'D4', 'B4', 'B4', 'C4', 'rest'  # nang da-hil sa-'yo
              ]

def createnote(noteName="A4", type="random", amp=0.5, beats=1.0, filter=None, cutoff=None, filename="defaultFileName"):
    
    # Initialize some values, let signal be empty first
    frequency = noteFreqs[noteName]
    duration = beats / 2
    sin_sig = thinkdsp.SinSignal(freq=0)
    
    # Add harmonics to the signal according to their Fourier Synthesis Coefficients
    
    for i in range(0, 8):  # delete if not fourier
        sin_sig += thinkdsp.SinSignal(freq=frequency*i, amp=amp*fourier_coeffs[type][i], offset=0)
    
    # Convert signal into wave to .wav file to AudioSegment to be mixed and played by the program
    wave = sin_sig.make_wave(duration=duration, start=0, framerate=44100)

    wave.write(filename=filename)
    audio = AudioSegment.from_wav(filename)

    audio.low_pass_filter(440)

    return audio

def createSpace(track, attack=100, release=100):
    for i in range(0, len(track) - 1):
        if track[i][0:2] == track[i + 1][0:2]:
            track[i] = track[i].fade_out(duration=release)
            track[i + 1] = track[i + 1].fade_in(duration=attack)


# grouping the message into two bits
def groupBits(message):
    two_bit.clear()
    for i in range(0, len(message)-1, 2):
        bit = message[i:i+2]
        two_bit.append(bit)
        print(bit)
    
    

# creating an array of audio segments      
def createseg(track_l, seg_track, digital_input):
    groupBits(digital_input)
    for x in range(0, len(track_l)):
        print(len(two_bit))
        
        if two_bit[x] == '10':
            beats = bt  
        elif two_bit[x] == '01':
            beats = bt/2
        elif two_bit[x] == '11':
            beats = bt*2
        else:
            beats = bt/4
        seg_track.append(createnote(track_l[x], beats=beats))
        print(track_l[x])
 

# mixing two tracks
def mix2tracks(track1, track2, message1, message2):
    seg_track1.clear()
    seg_track2.clear()
    createseg(track1, seg_track1, message1)
    createseg(track2, seg_track2, message2)
    
    createSpace(seg_track1, attack=50, release=50)
    createSpace(seg_track2, attack=50, release=50)
    song = AudioSegment.empty()
    

    for i in range(len(track1)):
        note1 = seg_track1[i]
        note2 = seg_track2[i]
        song += note1[:len(note1)].overlay(note2[:len(note2)])

    return song
    

part1 = mix2tracks(track1 = part1_note, track2 = part1_note_f, message1 = part1_message, message2= part1_message_long)
part2 = mix2tracks(track1 = part2_note, track2 = part2_note_f, message1 = part2_message, message2= part2_message_long)
part3 = mix2tracks(track1 = part3_note, track2 = part3_note_f, message1 = part3_message, message2= part3_message_long)
play(part1)
play(part1)
play(part2)
play(part2)
play(part3)
play(part3)
