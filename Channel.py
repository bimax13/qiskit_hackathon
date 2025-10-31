from qiskit import *
import Terminal

def SendQbits(fromA : Terminal, toB : Terminal):
    toB.qbits = fromA.qbits

def SendBasis(fromA : Terminal, toB : Terminal):
    toB.otherBasis = fromA.basis
