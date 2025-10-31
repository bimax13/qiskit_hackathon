from qiskit import *
import qiskit_aer
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np


class Sender:
    def __init__(self, n_bits):
        self.sender_bits = np.random.randint(2, size = n_bits)
        self.sender_bases = np.random.randint(2, size = n_bits)
        self._nbits = n_bits 

   

    def encode(self):
        circuits=[]
        for bit, basis in zip(self.sender_bits, self.sender_bases):
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

                


Alice = Sender(4)
Alice.encode()

plt.show()


def get_index_same_elements(base_a, base_b, bits):
    return[i for i, bit in enumerate(bits) if base_a[i] == base_b[i]]

def filter_unlikely_element(base_a, base_b, bits):
    return[bit for i, bit in enumerate(bits) if base_a[i] == base_b[i]]