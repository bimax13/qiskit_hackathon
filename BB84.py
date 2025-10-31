from qiskit import *
import numpy as np
from typing import List, Tuple
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def GenBitArr(num):
    return np.random.choice([0, 1], size=num).tolist()

def GenBasis(num_qubits):
    return GenBitArr(num_qubits)
    
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


def apply_noise(circuits: List[QuantumCircuit], noise_type: str = "none", noise_prob: float = 0.05) -> List[QuantumCircuit]:
    """Apply optional noise to each qubit circuit in the list."""
    noisy_circuits = []

    for qc in circuits:
        noisy_qc = qc.copy()  # make a copy to avoid modifying original

        # Apply noise probabilistically
        if noise_type != "none" and np.random.rand() < noise_prob:
            if noise_type == "bit-flip":
                noisy_qc.x(0)
            elif noise_type == "phase-flip":
                noisy_qc.z(0)
            elif noise_type == "depolarizing":
                gate = np.random.choice(["x", "y", "z"])
                if gate == "x":
                    noisy_qc.x(0)
                elif gate == "y":
                    noisy_qc.y(0)
                else:
                    noisy_qc.z(0)

        noisy_circuits.append(noisy_qc)

    return noisy_circuits

#print(BB84.getMatchingIndexes(Alice.basis, Bob.basis))

#def getMatchingIndexes(basisA, basisB):
#    return[i for i, bit in enumerate(basisB) if basisA[i] == basisB[i]]
def SiftAndMakeKey(base_a, base_b, bits):
    return[bit for i, bit in enumerate(bits) if base_a[i] == base_b[i]]