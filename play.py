import time
from tracks import *


#filter
part1 = part1.low_pass_filter(500)
part2 = part2.low_pass_filter(500)
part3 = part3.low_pass_filter(500)
part4 = part4.low_pass_filter(500)

#Lupang hiniran
play(part1) #I and II
play(part2) #III
play(part2) #III
play(part3) #IV
play(part4) #IV

    

