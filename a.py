import sys
import time
# print all the arguments
print(sys.argv)

with open('b', 'w') as f:
    f.write(str(sys.argv))
    f.write('\n')
    f.write(str(time.time()))
