from notes import *


lupang_hinirang = [G1, Gb1_eight, A1_sixt, G1, #Ba-yang Ma-gi-
                   D1, A1_eight, B1_eight, C2_eight,  #-liw per-las ng
                   B1_eight, A1_sixt, B1, G1_eight, rest_eight, #si-la-nga-nan
                   G1, Gb1_eight, A1_sixt,  G1,  #a-lab-ng-pu-
                   D1,A1_eight, B1_eight, C2_eight, #-so-sa-dib-dib-
                   B1_eight, A1_sixt, G1, rest] #-mo'y bu -hay
                    
lupang_hinirang_filler= [G1_long, Gb1_long, A1_long, G1_long, 
                          D1_long, A1_long, B1_long, C2_long, 
                          B1_long, A1_long, B1_long, G1_long, rest_eight,
                          G1_long, Gb1_long, A1_long,  G1_long, 
                          D1_long, A1_long, B1_long, C2_long, 
                          B1_long, A1_long, G1_long, rest]



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

song1 = mix2tracks(track1=lupang_hinirang, track2=lupang_hinirang_filler)