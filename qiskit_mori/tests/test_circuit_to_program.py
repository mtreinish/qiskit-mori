# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import pyquil as pq
import qiskit as qk

from qiskit_mori import circuit_to_program as cp
from qiskit_mori.tests import base


class TestCircuitToProgram(base.TestCase):

    def test_with_bell_circuit(self):
        # Qiskit Circuit
        qr = qk.QuantumRegister(2)
        bell = qk.QuantumCircuit(qr)
        bell.h(qr[0])
        bell.cx(qr[0], qr[1])
        prog = cp.circuit_to_program(bell)
        # Pyquil Program
        native_prog = pq.Program(pq.gates.H(0), pq.gates.CNOT(0, 1))
        self.assertEqual(prog, native_prog)
