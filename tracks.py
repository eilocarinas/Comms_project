from notes import *


lupang_hinirang = [G1, Gb1, A1, G1, D1, A1, B1, C2, B1, A1, B1, G1,
                   G1, Gb1, A1,  G1, D1, A1, B1, C2, B1, A1, G1]
lupang_hinirang_filler = [G1_long, Gb1_long, A1_long, G1_long, D1_long, A1_long, B1_long, C2_long, B1_long, A1_long, B1_long, G1_long,
                          G1_long, Gb1_long, A1_long,  G1_long, D1_long, A1_long, B1_long, C2_long, B1_long, A1_long, G1_long]

# Song 1: Jingle Bells

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
        note1 = track1[i]
        note2 = track2[i]
        song += note1[:len(note1)].overlay(note2[:len(note2)])
    return song

song1 = mix2tracks(track1=lupang_hinirang, track2=lupang_hinirang_filler)