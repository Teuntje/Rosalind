def readFasta(bestand):
    """Read fasta and save in fasta dictionary: {header: seq, n}"""
    fastaDic = {}
    with open(bestand) as inFile:
        for line in inFile:
            if line.startswith(">"):
                key = line.split(">")[1].strip()
                fastaDic[key] = []
            else:
                fastaDic[key].append(line.strip())
    fastaDic = {key: "".join(value) for key, value in fastaDic.items()}
    return fastaDic


def findOverlap(fastaDic):
    """Find overlap between the graphs and return these in a list"""
    fastaDic_vals = list(fastaDic.values())
    overlap = []
    # loop over the values of fastadic twice
    for seq1 in fastaDic_vals:
        for seq2 in fastaDic_vals:
            # if the first sequence isn't equal to the second
            if seq1 != seq2:
                # Overlap can be found with 3 nucleotides so divide
                # sequence into triplets
                for k in range(len(seq1)-3):
                    # Compare with sequence 2
                    if seq1[len(seq1)-k-3:len(seq1)-k] == seq2[k:k+3]:
                        for key, value in fastaDic.items():
                            if value == seq1:
                                keyy = key
                            elif value == seq2:
                                keyyy = key
                        overlap.append([keyy, keyyy])
    return overlap                    
    

def removeDuplicates(overlap):
    """Remove duplicates"""
    fset = set(frozenset(x) for x in overlap)
    lst = [list(x) for x in fset]
    return lst


if __name__ == "__main__":
    bestand = "overlap_graphs.txt"
    fastaDic = readFasta(bestand)
    overlap = findOverlap(fastaDic)
    lst = removeDuplicates(overlap)
    # Pretty print
    for i in lst:
        print(i[0], i[1])
