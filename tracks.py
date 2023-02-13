from notes import *


lupang_hinirang = [G4, Gb4, A4, G4, 'st', D4, A4, B4, C5, 'st', B4, A4, B4, G4]
lupang_hinirang_side = [G4_long, Gb4_long, A4_long, G4_long, 'st', D4_long, A4_long, B4_long, C5_long, 'st', B4_long, A4_long, B4_long, G4_long]

def createSpace (track = "track_1", attack = 50, release =50):
    track = noteFreqs
    

#ememe


def mixtracks (track_1, track_2):
    createSpace(track_1, attack = 50, release = 50)
    createSpace(track_2, attack = 50, release = 50)
    for i in range(len(track_1)):
        note1 = track_1[i]
        note2 = track_2[i]
        song = note1[:len(note1)].overlay(note2[:len(note2)])
        
    return song
