import Terminal
import BB84

def SendQbits(fromA : Terminal, toB : Terminal, noise_type: str = "none", noise_prob: float = 0.05):
    toB.qbits = BB84.apply_noise(fromA.qbits, noise_type, noise_prob)

def SendBasis(fromA : Terminal, toB : Terminal):
    toB.otherBasis = fromA.basis
