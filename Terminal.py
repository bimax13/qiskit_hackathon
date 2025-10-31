import BB84

class Terminal:
    def __init__(self):
        keys = None
        basis = None
        qbits = None
        cbits = None
        
    def GenBasis(self, n):
        self.basis = BB84.GenBasis(n)

    def GenQbits(self):
        self.cbits = BB84.GenBitArr(len(self.basis))
        self.qbits = BB84.GenQbits(self.cbits, self.basis)

        
    def ReceiveQbits(self, newQbits):
        self.qbits = newQbits

    def ReceiveBasis(self, newBasis):
        return 1==1

