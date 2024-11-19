# Monomer-extraction
A program to convert a full CSD recognized CIF file to molecular monomer XYZ file using the CSD and ASE Python libraries.

To ensure compatibility, verions of ASE and CCDC are:
ASE = 3.23.0
CCDC = 3.3.0

To create an environment ready for this code use:
```
conda create -n csdpy
conda install --channel=https://conda.ccdc.cam.ac.uk csd-python-api
conda install ase
```

To run the program optimally, ensure get_mon.py is in the folder with the cif file:
```
conda activate csdpy
python3 get_mon.py
```

Please enjoy and report any bugs found.
