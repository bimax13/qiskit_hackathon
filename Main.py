import BB84
from Terminal import Terminal
import Channel

nbits = 10

Alice = Terminal()
Bob = Terminal()

Alice.GenBasis(nbits)
Alice.GenQbits()

Channel.SendQbits(Alice, Bob)
print("Alice and Bob have same Qbits:", Alice.qbits == Bob.qbits)

Bob.GenBasis(nbits)


print("Alice's Basis:", Alice.basis)
print("Bob's Basis:  ", Bob.basis)


sift = BB84.getMatchingIndexes(Alice.basis, Bob.basis, [0,1,0,1,0,1,0,1,0,1])
key = BB84.siftAndMakeKey(Alice.basis, Bob.basis, [0,1,0,1,0,1,0,1,0,1])
print(sift)
print(key)