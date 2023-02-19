from notes import *

# quarter note represents 1 and eight note represents 0
part1= [G4, Gb4_eight, A4_eight, G4, #Ba-yang Ma-gi-
                   D4, A4_eight, B4_eight, C5_eight,  #-liw per-las ng
                   B4_eight, A4_eight, B4, G4_eight, rest_eight, #si-la-nga-nan
                   G4, Gb4_eight, A4_eight,  G4,  #a-lab-ng-pu-
                   D4,A4_eight, B4_eight, C5_eight, #-so-sa-dib-dib-
                   B4_eight, A4_eight, G4, rest,
                   G4, Gb4_eight, A4_eight, G4, #Ba-yang Ma-gi-
                   D4, A4_eight, B4_eight, C5_eight,  #-liw per-las ng
                   B4_eight, A4_eight, B4, G4_eight, rest_eight, #si-la-nga-nan
                   G4, Gb4_eight, A4_eight,  G4,  #a-lab-ng-pu-
                   D4,A4_eight, B4_eight, C5_eight, #-so-sa-dib-dib-
                   B4_eight, A4_eight, G4, rest_eight] #-mo'y bu -hay
part1_message = "100101101001010101011001011001011010010101"

for i in range(0, len(part1_message)):
   
   bit = int(part1_message[i])
   
   if bit == 1:
       bt = bt
   else:
       bt = bt/2 



part1_filler= [G3, Gb3_eight, A3_sixth, G3, #Ba-yang Ma-gi-
                   D3, A3_eight, B3_eight, C4_eight,  #-liw per-las ng
                   B3_eight, A3_sixth, B3, G3_eight, rest_eight, #si-la-nga-nan
                   G3, Gb3_eight, A3_sixth,  G3,  #a-lab-ng-pu-
                   D3,A3_eight, B3_eight, C4_eight, #-so-sa-dib-dib-
                   B3_eight, A3_sixth, G3, rest,
                   G3, Gb3_eight, A3_sixth, G3, #Ba-yang Ma-gi-
                   D3, A3_eight, B3_eight, C4_eight,  #-liw per-las ng
                   B3_eight, A3_sixth, B3, G3_eight, rest_eight, #si-la-nga-nan
                   G3, Gb3_eight, A3_sixth,  G3,  #a-lab-ng-pu-
                   D3,A3_eight, B3_eight, C4_eight, #-so-sa-dib-dib-
                   B3_eight, A3_sixth, G3, rest_eight] #-mo'y bu -hay


part2 = [G4_eight, Gb4_sixth, G4_eight, A4_eight, 
         A4_sixth, D4_eight, D4_sixth, A4_eight, 
         A4_sixth, D4_eight, D4_sixth,
         B4_eight, C5_sixth, D5_eight, E5_sixth, D5,
         G4_eight, Gb4_sixth, G4_eight, A4_eight, A4_sixth, D4_eight, D4_sixth, A4_eight, A4_sixth, D4_eight, D4_sixth,
         B4_sixth, C5_sixth, B4_sixth, A4_sixth, B4_sixth, A4_sixth, G4] 

part2_filler = [G4_long, Gb4_long, G4_eight, A4_long, A4_long, D4_long, D4_long, A4_long, A4_long, D4_long, D4_long,
                B4_long, C5_long, D5_long, E5_long, D5_long,
                G4_long, Gb4_long, G4_long, A4_long, A4_long, D4_long, D4_long, A4_long, A4_long, D4_long, D4_long,
                B4_long, C5_long, B4_long, A4_long, B4_long, A4_long, G4_long] 

part3 = [G4_eight, E4_sixth, G4_eight, C5, C5,    #Lu-pa ng a-raw
             D6, D6, E4_eight, D5_sixth, C5_eight, D5_sixth, E4,    #ng luwal-ha-ti't pag-sin-ta
             G4_eight, E4_eight, D5_eight, E4, C5, D5, B4_eight, B4_eight, C5, rest    #Bu-hay ay la-ngit sa pi-ling mo
             ]

part3_filler = [G4_long, E4_long, G4_long, C5_long, C5_long, #Lu-pa ng a-raw
                    D5_long, D5_long, E4_long, D5_long, C5_long, D5_long, E4_long, #ng luwal-ha-ti't pag-sin-ta
                    F4_long, E4_long, D5_long, E4_long, C5_long, D5_long, B4_long, B4_long, C5_long, rest #Bu-hay ay la-ngit sa pi-ling mo
                    ]

part4 = [G4_eight, E4_sixth, G4_eight, C5,
          C5, D5, D5, E4_eight, 
          D5_sixth, C5_eight, D5_sixth, E4, 
          Gb4_eight, E4_eight, D5_eight, E4, 
          C5, D5, B4_eight, B4_sixth, C5, rest
          ] 

part4_filler = [G4_long, E4_long, G4_long, C5_long, 
                    C5_long, D5_long, D5_long, E4_long, 
                    D5_long, C5_long, D5_long, E4_long,
          	        Gb4_long, E4_long, D5_long, E4_long, 
                    C5_long, D5_long, B4_long, B4_long, 
                    C5_long, rest
                   ] 

def createSpace(track, attack=100, release=100):
    for i in range(0, len(track) - 1):
        if track[i][0:2] == track[i + 1][0:2]:
            track[i] = track[i].fade_out(duration=release)
            track[i + 1] = track[i + 1].fade_in(duration=attack)

#creates function to mix two tracks
def mix2tracks(track1, track2):
    createSpace(track1, attack=50, release=50)
    createSpace(track2, attack=50, release=50)
    song = AudioSegment.empty()
    for i in range(len(track1)):
        note1 = track1[i]
        note2 = track2[i]
        song += note1[:len(note1)].overlay(note2[:len(note2)])
    return song
#mixing two tracks

part1 = mix2tracks(track1=part1, track2=part1)
part2 = mix2tracks(track1=part2, track2=part2_filler)
part3 = mix2tracks(track1=part3, track2=part3_filler)
part4 = mix2tracks(track1=part4, track2=part4_filler)