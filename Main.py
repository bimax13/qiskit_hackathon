import BB84
from Terminal import Terminal
import Channel

nbits = 20
noise = "none"
intercept = False

Alice = Terminal()
Bob = Terminal()

Alice.GenBasis(nbits)
Alice.GenQbits()
Channel.SendQbits(Alice, Bob, intercept, noise)

Bob.GenBasis(nbits)
Bob.MeasureQbits()

Channel.SendBasis(Bob, Alice)
Channel.SendBasis(Alice, Bob)

Alice.SiftAndMakeKey()
Bob.SiftAndMakeKey()


print("Alice's Key: ",Alice.key)
print("Bob's Key:   ",Bob.key)