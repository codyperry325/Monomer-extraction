# Monomer-extraction
A program to convert a full CSD recognized CIF file to molecular monomer XYZ file using the CSD and ASE Python libraries. This code DOES assume there is symmetrically equivalent monomers and thus, only one monomer XYZ file will be created.

To ensure compatibility, verions of ASE and CCDC are:
```
python = 3.11.5
ase = 3.23.0
csd-python-api = 3.3.0
```

To create an environment ready for this code use:

```
conda create -n csdpy
conda install --channel=https://conda.ccdc.cam.ac.uk csd-python-api
conda install -c conda-forge ase
```

You must have a CCDC license to use this code, if you have already installed the library it should not be a problem. 

To run the program optimally, ensure get_mon.py is in the folder with the cif file:
```
conda activate csdpy
python3 get_mon.py
```

Please enjoy and report any bugs found. I cannot gauruntee it will work with future version of python, ase or the csd api! :) 
