import re

gencode = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}


def fasta_reader(bestand):
    """return sequences and intronen from FASTA file"""
    sequences = []
    seq = []
    with open(bestand) as inFile:
        for line in inFile:
            line = line.strip()
            if line.startswith(">"):
                if seq != []:
                    sequences.append("".join(seq))
                    seq = []
            else:
                seq.append(line)
    sequences.append("".join(seq))

    dna = sequences[0]
    intronen = sequences[1:]
    return intronen, dna


def getmRNA(intronen, dna):
    """Extract mRNA from dna by removing introns"""
    for i in intronen:
        dna = dna.replace(i, "")
    return dna


def translate_dna(exons):
    """Translate mRNA into protein"""
    aa = []
    for i in range(0, len(exons), 3):
        if "_" not in gencode[exons[i:i+3]]:
            aa.append(gencode[exons[i:i + 3]])

    print("".join(aa))


if __name__ == '__main__':
    bestand = "rna_splicing2.txt"
    bestand = "rosalind_splc.txt"
    intronen, dna = fasta_reader(bestand)
    intronen.sort(reverse=True)
    mRNA = getmRNA(intronen, dna)
    translate_dna(mRNA)