from notes import *

part1= [G1, Gb1_eight, A1_sixth, G1, #Ba-yang Ma-gi-
                   D1, A1_eight, B1_eight, C2_eight,  #-liw per-las ng
                   B1_eight, A1_sixth, B1, G1_eight, rest_eight, #si-la-nga-nan
                   G1, Gb1_eight, A1_sixth,  G1,  #a-lab-ng-pu-
                   D1,A1_eight, B1_eight, C2_eight, #-so-sa-dib-dib-
                   B1_eight, A1_sixth, G1, rest,
                   G1, Gb1_eight, A1_sixth, G1, #Ba-yang Ma-gi-
                   D1, A1_eight, B1_eight, C2_eight,  #-liw per-las ng
                   B1_eight, A1_sixth, B1, G1_eight, rest_eight, #si-la-nga-nan
                   G1, Gb1_eight, A1_sixth,  G1,  #a-lab-ng-pu-
                   D1,A1_eight, B1_eight, C2_eight, #-so-sa-dib-dib-
                   B1_eight, A1_sixth, G1, rest_eight] #-mo'y bu -hay

part1_filler= [G1_long, Gb1_long, A1_long, G1_long, 
                D1_long, A1_long, B1_long, C2_long, 
                B1_long, A1_long, B1_long, G1_long, rest_eight,
                G1_long, Gb1_long, A1_long,  G1_long, 
                D1_long, A1_long, B1_long, C2_long, 
                B1_long, A1_long, G1_long, rest,
                G1_long, Gb1_long, A1_long, G1_long, 
                D1_long, A1_long, B1_long, C2_long, 
                B1_long, A1_long, B1_long, G1_long, rest_eight,
                G1_long, Gb1_long, A1_long,  G1_long, 
                D1_long, A1_long, B1_long, C2_long, 
                B1_long, A1_long, G1_long, rest_eight]


part2 = [G1_eight, Gb1_sixth, G1_eight, A1_eight, 
         A1_sixth, D1_eight, D1_sixth, A1_eight, 
         A1_sixth, D1_eight, D1_sixth,
         B1_eight, C2_sixth, D2_eight, E2_sixth, D2,
         G1_eight, Gb1_sixth, G1_eight, A1_eight, A1_sixth, D1_eight, D1_sixth, A1_eight, A1_sixth, D1_eight, D1_sixth,
         B1_sixth, C2_sixth, B1_sixth, A1_sixth, B1_sixth, A1_sixth, G1] 

part2_filler = [G1_long, Gb1_long, G1_eight, A1_long, A1_long, D1_long, D1_long, A1_long, A1_long, D1_long, D1_long,
                B1_long, C2_long, D2_long, E2_long, D2_long,
                G1_long, Gb1_long, G1_long, A1_long, A1_long, D1_long, D1_long, A1_long, A1_long, D1_long, D1_long,
                B1_long, C2_long, B1_long, A1_long, B1_long, A1_long, G1_long] 

part3 = [G1_eight, E1_sixth, G1_eight, C2, C2,    #Lu-pa ng a-raw
             D3, D3, E1_eight, D2_sixth, C2_eight, D2_sixth, E1,    #ng luwal-ha-ti't pag-sin-ta
             G1_eight, E1_eight, D2_eight, E1, C2, D2, B1_eight, B1_eight, C2, rest    #Bu-hay ay la-ngit sa pi-ling mo
             ]

part3_filler = [G1_long, E1_long, G1_long, C2_long, C2_long, #Lu-pa ng a-raw
                    D2_long, D2_long, E1_long, D2_long, C2_long, D2_long, E1_long, #ng luwal-ha-ti't pag-sin-ta
                    F1_long, E1_long, D2_long, E1_long, C2_long, D2_long, B1_long, B1_long, C2_long, rest #Bu-hay ay la-ngit sa pi-ling mo
                    ]

part4 = [G1_eight, E1_sixth, G1_eight, C2,
          C2, D2, D2, E1_eight, 
          D2_sixth, C2_eight, D2_sixth, E1, 
          Gb1_eight, E1_eight, D2_eight, E1, 
          C2, D2, B1_eight, B1_sixth, C2, rest
          ] 

part4_filler = [G1_long, E1_long, G1_long, C2_long, 
                    C2_long, D2_long, D2_long, E1_long, 
                    D2_long, C2_long, D2_long, E1_long,
          	        Gb1_long, E1_long, D2_long, E1_long, 
                    C2_long, D2_long, B1_long, B1_long, 
                    C2_long, rest
                   ] 

def createSpace(track, attack=100, release=100):
    for i in range(0, len(track) - 1):
        if track[i][0:2] == track[i + 1][0:2]:
            track[i] = track[i].fade_out(duration=release)
            track[i + 1] = track[i + 1].fade_in(duration=attack)

# Combines two audio tracks
note1 = []
note2 = []

def mix2tracks(track1, track2):
    createSpace(track1, attack=50, release=50)
    createSpace(track2, attack=50, release=50)
    song = AudioSegment.empty()
    for i in range(len(track1)):
        note1 = track1[i]
        note2 = track2[i]
        song += note1[:len(note1)].overlay(note2[:len(note2)])
    return song

part1 = mix2tracks(track1=part1, track2=part1_filler)
part2 = mix2tracks(track1=part2, track2=part2_filler)
part3 = mix2tracks(track1=part3, track2=part3_filler)
part4 = mix2tracks(track1=part4, track2=part4_filler)