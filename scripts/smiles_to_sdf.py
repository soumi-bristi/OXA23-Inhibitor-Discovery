from rdkit import Chem
from rdkit.Chem import AllChem
import os

smiles_list = [
    "COc1ccc(C2=NOC(c3ccc(F)c(C(=O)O)c3F)C2)cc1",
    "O=C(O)c1c(F)cc(F)cc1C1CC1c1ccccc1F",
    "O=C(O)Cc1ccc(-c2ccc(F)c(C(=O)O)c2F)o1",
    "O=C(O)c1ccc2c(c1)CCCC2c1ccc(F)c(C(=O)O)c1F",
    "O=C(O)c1ccc2c(c1)C1Oc3c(F)ccc(F)c3C1CO2",
    "Cc1onc(-c2ccc(F)c(F)c2)c1C(=O)O",
    "Cc1onc(-c2cc(F)ccc2F)c1C(=O)O",
    "O=C(O)C1CC2C(c3ccc(F)c(F)c3)=NOC12",
    "Cc1coc(-c2cc(F)ccc2F)c1C(=O)O",
    "O=C(O)c1ccc(-c2cccc(F)c2C(=O)O)o1",
    "O=C1CC(c2ccc(F)cc2F)C(C(=O)O)C=N1",
    "CC(Oc1ccc(F)c(Cl)c1C(=O)O)C(=O)O",
    "O=C(O)c1c(F)ccc(F)c1S(=O)(=O)NC1CC1",
    "O=C(O)C1CCC(=O)C1c1cc(F)ccc1F",
    "O=C(O)c1ccc(Br)c(F)c1C(=O)O",
    "O=C(O)c1ccc(F)c(F)c1C1CCCO1",
    "O=C(O)c1ccc(F)c(C2CC(C(=O)O)C2)c1",
    "O=C(O)c1cc2c(C(=O)O)c(F)ccc2s1",
    "Cc1oc(-c2ccccc2F)c(C(=O)O)c1O",
    "CS(=O)(=O)Nc1ccc(F)c(C(=O)O)c1F",
    "CCC1COc2c(ccc(F)c2C(=O)O)C1",
    "Cc1oc2c(C(=O)O)ccc(F)c2c1C(=O)O",
    "O=C(O)CCC1COc2c(F)cccc21",
    "CC(CCO)Oc1ccc(F)c(C(=O)O)c1F",
    "CN1C(=O)CC(c2ccc(F)c(F)c2F)C1C(=O)O",
    "O=C(O)c1c(F)ccc2c1Oc1ccccc1C2O",
    "COc1c(F)ccc2c1OCC(O)C2NC(C)=O",
    "CCOc1c(C(=O)O)ccc(F)c1C(=O)O",
    "NC(=O)CC1CC1c1cc(F)ccc1F",
    "O=C(O)COc1ccc(F)c(C(=O)O)c1F",
    "O=C(O)COc1c(F)ccc(F)c1C(=O)O",
    "O=C(O)COc1c(F)ccc(F)c1C(=O)O",
    "O=C(O)C1CC(C(=O)O)c2cc(F)ccc2O1",
    "O=C(O)c1c(F)ccc2c(F)cc(F)cc12",
    "O=C(O)c1c(OC(F)(F)F)ccc(F)c1F",
    "O=C(O)c1c(F)ccc2c1-c1ccccc1C2O",
    "O=C(O)c1c(F)ccc(S(=O)(=O)O)c1Br",
    "COc1ccc(F)c(OC)c1C(=O)O",
    "CS(=O)(=O)c1cccc(F)c1C(=O)O",
    "O=C(O)c1c(F)ccc2c1NC(c1ccc(F)cc1)C1CC=CC21"
]

output_folder = 'molecules_3d_separate'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for i, smi in enumerate(smiles_list, 1):
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        print(f"Could not parse SMILES {i}: {smi}")
        continue
    
    
    mol = Chem.AddHs(mol)
    
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())
    
    AllChem.UFFOptimizeMolecule(mol)
    
    mol.SetProp('_Name', f'Molecule_{i}')
    
    file_path = os.path.join(output_folder, f'Molecule_{i}.sdf')
    writer = Chem.SDWriter(file_path)
    writer.write(mol)
    writer.close()

print(f"Created {len(smiles_list)} separate SDF files in the '{output_folder}' folder!")
