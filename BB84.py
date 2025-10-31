from qiskit import *
import numpy as np
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def GenBitArr(num, seed=None):
    if seed is not None:
        np.random.seed(seed)
    return np.random.choice([0, 1], size=num)

def GenBasis(num_qubits, seed=None):
    return GenBitArr(num_qubits, seed)
    
def GenQbits(bitArr, basisArr):
    circuits=[]
    for bit, basis in zip(bitArr, basisArr):
        qc = QuantumCircuit(1,1)
        if basis==0:
            if bit == 1:
                qc.x(0)
        else:
            if bit == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qc.draw('mpl')
        circuits.append(qc)
    return circuits

def getMatchingIndexes(basisA, basisB, bits):
    return[i for i, bit in enumerate(bits) if basisA[i] == basisB[i]]

def siftAndMakeKey(base_a, base_b, bits):
    return[bit for i, bit in enumerate(bits) if base_a[i] == base_b[i]]