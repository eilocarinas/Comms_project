from notes import *


lupang_hinirang = [G4, Gb4, A4, G4, D4, A4, B4, C5, B4, A4, B4, G4]
lupang_hinirang_filler = [G4_long, Gb4_long, A4_long, G4_long, D4_long, A4_long, B4_long, C5_long, B4_long, A4_long, B4_long, G4_long]

# Envelopes
# .fade_in and .fade_out serve as crossfaders for DJs in combining multiple audio signals
# But in this case, I convert each note into its own signal
# So .fade_in serves as the "Attack" time on the ADSR envelope
# And .fade_out serves as the "Release" time on the ADSR envelope
# Creates spacing between consecutive notes that are the same by adding attack and release

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
        note1 = lupang_hinirang[i]
        note2 = track2[i]
        song += note1[:len(note1)].overlay(note2[:len(note2)])
    return song

song1 = mix2tracks(track1=lupang_hinirang, track2=lupang_hinirang_filler)