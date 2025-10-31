from qiskit import QuantumCircuit
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


def err_rate_calculation(key_a, key_b):
    error = sum(a != b for a,b in zip(key_a, key_b) )
    err_rate = error/len(key_a)
    return err_rate

def measure_qubits(circuits, bases):
    measured_circuits = []
    for qc, basis in zip(circuits, bases):
        measured_qc = qc.copy()
        if basis == 1:  # For X-basis, apply H before measurement.
            measured_qc.h(0)
        measured_qc.measure(0, 0)
        measured_circuits.append(measured_qc)
    return measured_circuits

def eavesdrop(circuits, eve_bases):
    intercepted = []
    for qc, basis in zip(circuits, eve_bases):
        new_qc = qc.copy()
        if basis == 1:
            new_qc.h(0)
        new_qc.measure(0, 0)
        # simulate collapse + resend
        intercepted.append(new_qc)
    return intercepted

