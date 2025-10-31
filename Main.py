import BB84
from Terminal import Terminal
import Channel

nbits = 10

Alice = Terminal()
Bob = Terminal()

Alice.GenBasis(nbits)
Alice.GenQbits()
Channel.SendQbits(Alice, Bob)

Bob.GenBasis(nbits)
Bob.MeasureQbits()

Channel.SendBasis(Bob, Alice)
Channel.SendBasis(Alice, Bob)

Alice.SiftAndMakeKey()
Bob.SiftAndMakeKey()
print("Alice's Sent bits:",Alice.cbits)
print("Bob's Measured:   ",Bob.cbits)
print("Alice's Key:      ",Alice.key)
print("Bob's Key:        ",Bob.key)