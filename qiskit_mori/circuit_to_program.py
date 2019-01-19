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

import pyquil
from pyquil import gates


def get_mapped(name):
    gate = getattr(gates, name.upper(), None)
    if gate:
        return gate
    if name == 'cx':
        return gates.CNOT
    if name == 'ccx':
        return gates.CCNOT
    return None


def circuit_to_program(circuit):
    """Take in a qiskit QuantumCircuit object and return a PyQuil Program.

    Args:
        circuit (qiskit.QuantumCircuit): The input QuantumCircuit object
    Returns:
        pyquil.Program: The pyquil Program object for the input circuit

    """
    qubits = 0
    clbits = 0
    qregs_offset = {}
    raw_qoffset = 0
    for qreg in circuit.qregs:
        qubits += qreg.size
        qregs_offset[qreg.name] = raw_qoffset
        raw_qoffset = qreg.size
    cregs_offset = {}
    raw_coffset = 0
    for creg in circuit.cregs:
        clbits += creg.size
        cregs_offset[creg.name] = raw_coffset
        raw_coffset = creg.size
    prog = pyquil.Program()
    for inst in circuit.data:
        func = get_mapped(inst.name)
        qargs = [qregs_offset[x[0].name] + x[1] for x in inst.qargs]
        cargs = [cregs_offset[x[0].name] + x[1] for x in inst.cargs]
        # NOTE(mtreinish): In qiskit-terra >=0.8.0 inst.param will be renamed
        # inst.params
        params = inst.param + qargs + cargs
        prog += func(*params)
    return prog
