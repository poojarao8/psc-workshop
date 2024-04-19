To run CUDA-Q scripts interactively on Bridges-2 on a single gpu.

Step 1:
Login into the Bridges-2 machine.
$ ssh <username>@bridges2.psc.edu

Step 2:
Pull the repo and change to that directory.
$ git pull https://github.com/poojarao8/psc-workshop.git
$ cd psc-workshop

Step 3:
Request an interactive gpu allocation.
$ interact -gpu

Step 4: 
Run a CUDA-Q script.
$ apptainer exec --nv /opt/packages/cuda-quantum/v0.7.0/cuda-quantum_0.7.0.sif /usr/bin/python my_first_kernel.py --target nvidia
