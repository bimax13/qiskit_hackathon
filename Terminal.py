import BB84
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


class Terminal:
    key = None
    basis = None
    otherBasis = None
    qbits = None
    cbits = None # aka measured bits
        
    def GenBasis(self, n):
        self.basis = BB84.GenBasis(n)

    def GenQbits(self):
        self.cbits = BB84.GenBitArr(len(self.basis))
        self.qbits = BB84.GenQbits(self.cbits, self.basis)

    def MeasureQbits(self, noise_type: str = "none", noise_prob: float = 0.05):
        backend = AerSimulator()
        measured_bits = []

        for qc, basis in zip(self.qbits, self.basis):
            noisy_qc = qc.copy()

            # Apply optional noise
            noisy_qc = BB84.apply_noise(noisy_qc, noise_type, noise_prob)

            # Apply Bob's measurement basis
            if basis == 1:  # X-basis
                noisy_qc.h(0)

            # Measure
            noisy_qc.measure(0, 0)
            transpiled_qc = transpile(noisy_qc, backend)
            job = backend.run(transpiled_qc, shots=1, memory=True)
            result = job.result()
            bit = int(result.get_memory()[0])
            measured_bits.append(bit)
        
        self.cbits = measured_bits
        return measured_bits
        
    def SiftAndMakeKey(self):
        self.key = [bit for i, bit in enumerate(self.cbits) if self.basis[i] == self.otherBasis[i]]

