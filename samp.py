part1_message = "100101101001010101011001011001011010010101"
part1="10000111111110000101111100010011000111110001100000001000011111111000010111110001001100011111100000001000011111111000010111110001001100011111000110000000100001111111100001011111000100110001111110000000"
four_bit = []
for i in range(0, len(part1)-1, 4):
    bit = part1[i:i+5]
    four_bit.append(bit)
    print(bit)
#print(two_bit)

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



