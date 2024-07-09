# scripts4arthur

## Utilisation

Ce pipeline a été testé avec Ubuntu 20.04 et Debian 11. Aucun test n'a été effectuer avec MacOS ou Windows.

## Environnement

Afin de pouvoir exécuter chacune des étapes, il est nécessaire de construire un environnement conda avec environment.yaml. Ce fichier conteient tous les outils, langages et modules (python) utilisé  dans ce pipeline.

```bash
conda env create -f environment.yml

conda activate scripts4arthure
```

## Descriptions du pipelines

Ce pipeline à pour obtective de construire un ou plusieurs réseaux de similarité (SSNs) à partir d'un alignement pairwaise réalisé avec diamond blastp

1. Concaténation des fichiers  fasta

S'il y a plusieurs fichier, il est nécessaire de concaténer tous les fichiers fasta en un seul fichier fasta.

```bash
cat *.fasta > all.fasta
```

2. Pairwaise alignment

AALignement par pair avec diamond all vs all.

```bash
bash diamond.sh all.fasta
```

3. Filtration des alignement

Filtration des alignement obtenu avec diamond e fonction de 3 paramète identité, overlap et evalue.

```bash
filter.py
```

4. diamond 2 graph 



5. Attributes

6. Vertices

7. Network


## Example 

Des fichiers de test sont disponible dans les répertoire `annotation/` et `fasta/`.

Les résultats du test seront disponible dans le répertoire `results`.

1. Préparation du répertoire

```bash
git clone link && cd scripts4arthure
```

2. Environnement de développement

Cette environnement peut être construit avec Conda ou Mamba

```bash
# With Conda

conda env create -f environment.yml
conda activate scripts4arthure

# With Mamba

mamba env create -f environment.yml
conda activate scripts4arthure
```

3. Concaténation des fichiers fasta.

```bash
cat fasta/* > results/all.fasta
```

4. Diamond makedb & BLASTp

```bash
./scripts/diamond.sh results/all.fasta results/diamondDB results/diamond_alignment.tsv
```

5. Filtration des alignemnts
 
```bash
./scripts/filter.py results/diamond_alignment.tsv 80 80 1e-05 results/
```
 
6. Sequence annotation
 
Créer un tableau avec les annotations pour toutes les séquences
 
ATTENTION, 1 colonne correspond à 1 et 1 seule base de données d'annotation, et la première colonne contient obligatoire les identifiant des séquences annoté. 
 
il est bien entendu possible de créer autant de table qu'il y a de type d'annotation.
 
- première étape, créer une liste de toutes les séquences
 
conserver uniquement la partie conservé par diamond blastp afin de pouvoir effectuer un match
 
```bash
./scripts/sequence_list.sh results/all.fasta results/sequence_list.txt 
```

- troisième étape, concaténer toutes les tables d'annotations en 1 seul.

Dans cette exemple noius avons créer une table pour la banque de données Pfam et une table pour la banque de données CATH/Gene3D

vous trouverez les tables utilisé danscette partie dans le dossier `annotations/pfam`et dans annotations/gene3d`

ajoute également un identifiant pour chaque séquence
 
```bash
# Pfam
./scripts/merge.R annotations/pfam/pfam_annotation.tsv results/sequence_list.txt pfam results/
 
# CATH/Gene3D
./scripts/merge.R annotations/gene3d/gene3d_annotation.tsv results/sequence_list.txt gene3d results/
```

- quatrième étape, même étape que l'étape 2 mais avec uniquement les séquences qui ont passé le filtre
 
nécessite une étape supplémentaire afin de récupéré les noms des séquences
 

 
 
 
 
 
 
 
