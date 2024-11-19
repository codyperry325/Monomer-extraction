from ase.io import read,write
import glob
from ccdc import io
import os

if __name__ == "__main__":
    files=glob.glob("*.cif")
    for file in files:
        mol_reader = io.MoleculeReader(file)
        reader = mol_reader[0]
        atoms = reader.atoms
        mol = reader.components[0]
        writer = io.MoleculeWriter("temp.cif")
        writer.write(mol)
        monomer = read("temp.cif")
        write("monomer.xyz",monomer)
        os.remove("temp.cif")