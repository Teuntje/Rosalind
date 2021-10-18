

def read_fasta(bestand):
    """Return the sequence from the FASTA file"""
    sequence = ""
    with open(bestand) as inFile:
        for line in inFile:
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence


def reverse_complement(seq):
    """Return the reverse complement of the sequence"""
    seq = seq.replace("T", "U")
    seq = seq.replace("A", "T")
    seq = seq.replace("U", "A")
    seq = seq.replace("G", "V")
    seq = seq.replace("C", "G")
    seq = seq.replace("V", "C")
    return seq[::-1]


def palindrome(seq):
    """Check all palindromes in the sequence. These are potential
    restriction sites
    """
    palindromes = []
    # Loop over the full length of the sequence
    for i in range(len(seq)):
        # Work in steps, palindrome can range in length: 4 until 12
        for steps in range(4, 13):
            # Check if the length of the sequence is bigger than 3
            if len(seq[i:i+steps]) > 3:
                sequence = seq[i:i+steps]
                rev_com = reverse_complement(sequence)
                # Compare the reverse complement with the sequence
                if rev_com == sequence:
                    # Check if the range is not in the list
                    # --> add to list
                    if [i+1, len(sequence)] not in palindromes:
                        palindromes.append([i+1, len(sequence)])
    palindromes.sort(reverse=False)

    # Pretty print
    for el in palindromes:
        el = [str(el[0]), str(el[1])]
        print(" ".join(el))


if __name__ == '__main__':
    bestand = "palindrome.txt"
    bestand = "rosalind_revp.txt"
    seq = read_fasta(bestand)
    palindrome(seq)