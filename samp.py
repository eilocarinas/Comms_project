part1_message = "100101101001010101011001011001011010010101"
part1="10000111111110000101111100010011000111110001100000001000011111111000010111110001001100011111100000001000011111111000010111110001001100011111000110000000100001111111100001011111000100110001111110000000"
four_bit = []
part1_note = ['G4', 'Gb4', 'A4', 'G4',
                'D4', 'A4', 'B4', 'C5',
                 'B4', 'A4', 'B4', 'G4', 'rest',
                 'G4', 'Gb4', 'A4',  'G4', 
                 'D4','A4', 'B4', 'C5' ] 
print(len(part1_note))
for i in range(0, len(part1)-1, 4):
    bit = part1[i:i+4]
    four_bit.append(bit)
    #print(bit)
#print(two_bit)
print(len(four_bit))
for i in range(0, len(four_bit)):
    print(four_bit[i])
print(four_bit.__len__())
print(four_bit)
# 4th octave

A4 = '1111'
B4 = '0001'
Bb4 = '0010'
C4 = '0011'
D4 = '0101'
E4 =  '0110'
F4 ='0110'
Gb4 ='0111'
G4 = '1000'
C5 = '1001'
rest = '0000'

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

print("part1")
part1_note.clear()
print(len(part1_message))
print(len(part1_note))
print(len(part1_note_f))
print(len(part1_message_long))
print("part2")
print(len(part2_message))
print(len(part2_note))
print(len(part2_note_f))
print(len(part2_message_long))
print("part3")
print(len(part3_message))
print(len(part3_note))
print(len(part3_note_f))
print(len(part3_message_long))
two_bit = []
def groupBits(message):
    two_bit.clear()
    print(two_bit)
    for i in range(0, len(message)-1, 2):
        bit = message[i:i+2]
        two_bit.append(bit)
        print(bit)
groupBits(part1_message)
groupBits(part2_message)