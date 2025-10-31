from qiskit import *
import Terminal

def SendQbits(fromA : Terminal, toB : Terminal):
    toB.ReceiveQbits(fromA.qbits)

def SendBasis(fromA : Terminal, toB : Terminal):
    toB.ReceiveBasis(fromA.basis)
