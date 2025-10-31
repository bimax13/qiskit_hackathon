import Terminal
import BB84

def eavesdrop(qbits):
    eve_bases = BB84.GenBasis(len(qbits))
    intercepted = []
    for qc, basis in zip(qbits, eve_bases):
        new_qc = qc.copy()
        if basis == 1:
            new_qc.h(0)
        new_qc.measure(0, 0)
        # simulate collapse + resend
        intercepted.append(new_qc)
    return intercepted

def SendQbits(fromA: Terminal, toB: Terminal, intercept: bool, noise_type: str = "none", noise_prob: float = 0.05):
    noisyQbits = BB84.apply_noise(fromA.qbits, noise_type, noise_prob)
    toB.qbits = noisyQbits if (not intercept) else eavesdrop(noisyQbits)

def SendBasis(fromA : Terminal, toB : Terminal):
    toB.otherBasis = fromA.basis

# def SendBasis(fromA : Terminal, toB : Terminal):
#     toB.otherBasis = fromA.basis
