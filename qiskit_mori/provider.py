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

import collections

from pyquil import api
from qiskit import providers

from qiskit_mori import backends


class MoriProvider(providers.BaseProvider):
    """Provider for remote Rigetti Forest backends

    This class is the entry point for handling backends from Forest, allowing
    using different accounts.
    """
    def __init__(self):
        super(MoriProvider, self).__init__()
        self._forest_connections = collections.OrderedDict()

    def backends(self, name=None, filters=None, **kwargs):
        """Return all backends accessible via Mori provider."""
        pyquil_backends = api.list_quantum_computers()
        qiskit_backends = []
        for dev in pyquil_backends:
            backend = backends.create_backend(dev, self)
            if backend:
                qiskit_backends.append(backend)
        return providers.providerutils.filter_backends(qiskit_backends,
                                                       filters)
