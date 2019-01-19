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

from pyquil import api
from qiskit import converters
from qiskit import providers
from qiskit.providers import models

from qiskit_mori import circuit_to_program as cp


def create_backend(device_name, provider):
    try:
        dev = api.get_qc(device_name)
    except Exception:
        return None
    n_qubits = int(len(dev.qubits()))
    basis_gates = ''
    gates = [models.GateConfig()]
    if isinstance(dev.qam, api.QPU):
        simulator = False
    else:
        simulator = True
    max_shots = 1024
    conf = models.BackendConfiguration(
        device_name, '0.0.1', n_qubits, basis_gates, gates, False, simulator,
        False, False, False, max_shots)
    return MoriBackend(conf, provider, dev)


class MoriBackend(providers.BaseBackend):

    def __init__(self, configuration, provider, qc):
        super(MoriBackend, self).__init__(provider=provider,
                                          configuration=configuration)
        self.pyquil_qc = qc

    def run(self, qobj):
        circ = converters.qobj_to_circuits(qobj)
        prog = cp.circuit_to_program(circ)
        executable = self.pyquil_qc.compile(prog, False, False)
        return self.pyquil_qc.run(executable)
