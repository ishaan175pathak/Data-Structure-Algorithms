def reversing(S,start,end):
    if start < end:
        S[start],S[end-1] = S[end-1],S[start]
        start += 1
        end -= 1
        reversing(S,start,end)

import random as rand

S = list()

for a in range(5):
    num = rand.randint(0,20)
    S.append(num)

print(S)
reversing(S,0,len(S))
print(S)