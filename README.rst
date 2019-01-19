=======================================================
Qiskit Mori: A Qiskit Provider for the Rigetti Platform
=======================================================

This project strives to be a bridge to enable using Qiskit with Rigetti's
platform. It provides a Qiskit Terra backend provider for Rigetti
backends that can be used like any other Qiskit backend provider. It works
by converting the native Qiskit objects (QuantumCircuit, etc) into pyquil
constructs and then making the equivalent pyquil api calls to run and deal with
results as expected.

Current Status
--------------

Right now this is just the scaffolding to start. Running anything with Rigetti's
platform requires either running binary proprietary blobs locally for their
simulator or using their hosted solutions. I do not have either setup (and have
little desire to do either), so this likely won't progress much further beyond
this rough proof of concept. However, if someone with access would like to
contribute so we can move things forward feel free to submit a PR, open an
issue, or reach out to me.
