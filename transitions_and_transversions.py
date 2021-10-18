
def fasta_reader(bestand):
    """Extract sequences from FASTA file"""
    seqs = []
    seq = []
    with open(bestand) as inFile:
        for line in inFile:
            if not line.startswith(">"):
                seq.append(line.strip())
            else:
                if seq != []:
                    seqs.append("".join(seq))
                    seq = []
    seqs.append("".join(seq))
    return seqs


def transitions_transversions(seqs):
    """Calcultate the transition transversion rate"""
    transitions = 0
    transversions = 0
    for i in range(len(seqs[0])):
        seq1 = seqs[0][i]
        seq2 = seqs[1][i]
        # Compare the two sequences for each position.
        # Ignore the nucleotides that are equal
        if seq1 == seq2:
            continue
        # Count the number of transitions
        elif seq1 == "A" and seq2 == "G" or seq1 == "G" and seq2 == "A" or\
            seq1 == "C" and seq2 == "T" or seq2 == "C" and seq1 == "T":
            transitions += 1
        # Count the number of transversions
        else:
            transversions+= 1
            
    print(transitions/transversions)


if __name__ == '__main__':
    bestand = "transitions_and_transversions.txt"
    bestand="rosalind_tran.txt"
    seqs = fasta_reader(bestand)
    transitions_transversions(seqs)