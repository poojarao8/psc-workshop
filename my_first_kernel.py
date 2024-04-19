# To run: python my_first_kernel.py

import cudaq

# We begin by defining the `Kernel` that we will construct our
# program with.
@cudaq.kernel
def my_first_kernel():
    '''
    This is our first CUDA Quantum kernel.
    '''
    # Next, we can allocate qubits to the kernel via `qvector(num_qubits)`.
    # It will return a single qubit.
    qubit = cudaq.qubit()

    # Now we can begin adding instructions to apply to this qubit!
    # Here we'll just add every non-parameterized
    # single qubit gate that is supported by CUDA Quantum.
    h(qubit)
    x(qubit)
    y(qubit)
    z(qubit)
    t(qubit)
    s(qubit)

    # Next, we add a measurement to the kernel so that we can sample
    # the measurement results on our simulator!
    mz(qubit)

# Draw the circuit
print(cudaq.draw(my_first_kernel))

# Finally, we can execute this kernel on the state vector simulator
# by calling `cudaq.sample`. This will execute the provided kernel
# `shots_count` number of times and return the sampled distribution
# as a `cudaq.SampleResult` dictionary.
result = cudaq.sample(my_first_kernel)

# Now let's take a look at the `SampleResult` we've gotten back!
print(result)
