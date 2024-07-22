# for loops = execute a block of code a fixed number of times.
#                     You can iterate over a range, string, sequence, etc.
import time

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)