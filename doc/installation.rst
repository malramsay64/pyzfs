.. _installation:

============
Installation
============

**PyZFS** uses the **mpi4py** package for parallelization. An existing MPI implementation (e.g. **MPICH** or **OpenMPI**) is required to install **mpi4py** and **PyZFS**. Many supercomputers provide modules for pre-compiled MPI implementations. To install MPI manually (taking **MPICH** as example), execute the following command on Linux

.. code:: bash

   $ sudo apt-get install mpich libmpich-dev

or the following command on Mac

.. code:: bash

   $ brew install mpich

**PyZFS** can be installed by **pip**. First, clone the git repository into a local directory

.. code:: bash

   $ git clone https://github.com/hema-ted/pyzfs.git

Then, execute **pip** in the folder containing  **setup.py**

.. code:: bash

   $ pip install -e .

Since **PyZFS** may be executed with **python -m** (see :ref:`tutorial`), it is recommended to install it in editable mode (-e) and add the code path to the **PYTHONPATH** by appending the following command to **.bashrc** file

.. code:: bash

   $ export PYTHONPATH=$PYTHONPATH:path/to/pyzfs

Note that it is necessary for the path of **PyZFS** to be included in the **PYTHONPATH** for the **python -m** command to find **PyZFS**.

**PyZFS** depends on the following packages, which will be installed automatically if installed through **pip**

   - ``numpy``
   - ``scipy``
   - ``mpi4py``
   - ``h5py``
   - ``ase``
   - ``lxml``

**PyZFS** is designed to be compatible with both Python 2 and Python 3. However, to run **PyZFS** with Python 2 one may need to build certain legacy versions of dependencies such as **ase**.
