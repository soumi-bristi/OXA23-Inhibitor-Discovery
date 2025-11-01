# CADD-Driven Ligand Discovery Targeting OXA-23 Carbapenemase

## Project Overview

This project leverages Computer-Aided Drug Design (CADD) strategies to generate, evaluate, and identify novel ligands targeting the OXA-23 carbapenemase enzyme—a key resistance factor in *Acinetobacter baumannii*. The workflow integrates deep learning-based molecular generation, molecular docking, and ADMET profiling.

## Methodology

### 1. Ligand Generation with REINVENT
- **Platform**: Linux-based REINVENT implementation
- **Strategy**: Staged reinforcement learning approach
- **Training Configuration**: 
  - Stage 1: 500 training steps
  - Stage 2: 500 training steps
  - Batch size: 64 molecules per step
- **Output**: Top 40 candidate ligands selected from Stage 2

### 2. Molecular Processing & Docking
- **Format Conversion**: SMILES to 3D SDF conversion using RDKit (Python)
- **Docking Protocol**: PyRx (AutoDock Vina engine) against OXA-23 carbapenemase
- **Selection Criteria**: Binding affinity threshold ≤ -7.5 kcal/mol
- **Filtered Results**: 9 high-affinity ligands identified

### 3. Structural Analysis
- **Visualization Tool**: Discovery Studio Visualizer
- **Lead Compound**: Molecule 3 emerged as top candidate
- **Key Interactions**: Strong hydrogen bonding with Ser79 and contacts with Thr217, Ala220, Lys222, Val123

### 4. ADMET Profiling
- **Assessment Tool**: SwissADME platform
- **Lead Molecule Properties**:
  - High gastrointestinal absorption
  - Blood-brain barrier non-permeable
  - Lipinski's Rule of Five compliant
  - Clean PAINS profile
  - Favorable synthetic accessibility

## Key Outcomes

- **Lead Candidate**: Molecule 3 demonstrated optimal binding affinity and drug-like properties
- **Success Rate**: 22.5% of top candidates achieved high-affinity binding
- **Drug-likeness**: Lead compound passed all major ADMET filters
- **Target Engagement**: Strong interaction profile with OXA-23 active site residues

## Technologies Used

- **REINVENT**: AI-driven molecular generation (Linux)
- **RDKit**: Chemical informatics and structure processing (Python)
- **PyRx**: Virtual screening and molecular docking (AutoDock Vina engine)
- **Discovery Studio**: Protein-ligand interaction analysis
- **SwissADME**: Pharmacokinetic property prediction

## Useful Links

- **REINVENT GitHub**: https://github.com/MolecularAI/REINVENT4.git
- **RDKit Documentation**: https://www.rdkit.org/docs/
- **SwissADME**: http://www.swissadme.ch/


## Significance

This project demonstrates a complete computational pipeline for targeting antibiotic resistance mechanisms, specifically the OXA-23 carbapenemase that confers resistance in *Acinetobacter baumannii*. The integration of AI-generated molecules with traditional CADD approaches provides a promising strategy for discovering novel antimicrobial agents.

## Citations

### REINVENT Framework
Genheden, S., Thakkar, A., Chadimová, V., Reymond, J. L., Engkvist, O., & Bjerrum, E. J. (2020).
REINVENT 4.0: Modern AI–driven generative molecule design.
arXiv preprint arXiv:2312.10688.


### Additional REINVENT Reference
Blaschke, T., Arús-Pous, J., Chen, H., Margreitter, C., Tyrchan, C., Engkvist, O., ... & Bjerrum, E. J. (2020).
REINVENT 2.0: an AI tool for de novo drug design.
Journal of Chemical Information and Modeling, 60(12), 5918-5922.


### RDKit
RDKit: Open-source cheminformatics. https://www.rdkit.org


### AutoDock Vina
Trott, O., & Olson, A. J. (2010). AutoDock Vina: improving the speed and accuracy of docking
with a new scoring function, efficient optimization, and multithreading.
Journal of Computational Chemistry, 31(2), 455-461.



### PyRx
Dallakyan, S., & Olson, A. J. (2015). Small-molecule library screening by docking with PyRx.
In Chemical biology (pp. 243-250). Humana Press.


### SwissADME
Daina, A., Michielin, O., & Zoete, V. (2017). SwissADME: a free web tool to evaluate
pharmacokinetics, drug-likeness and medicinal chemistry friendliness of small molecules.
Scientific Reports, 7(1), 42717.

## License

This project uses REINVENT under its original license. Results presented are for academic and educational purposes only.