import re


def findMotif(seq, motif):
    """Find a motif in a sequence"""
    new_motif = "(?={})".format(motif)
    locations = [str(m.start()+1) for m in re.finditer(new_motif, seq)]
    return locations
    

if __name__ == "__main__":
    seq = "GATTTGTGTGGTTGTGTGGTGTAGCGACGCGTGTGTGGGGGTGTGTGGTGTGTGGAACCTGTGTGGGTATGTGTGGCGTTCTGTGTGGGAGCAGTGTGTGGTGTGTGTGGCATGTGTGGTGTGTGGTGTGTGGTTGTGTGGTACGACGAGATGTAATTTGTGTGGGATGTGTGGGCCACTGTGTGGCACGACTTGTGTTATGTGTGGTGTGTGGTTGATGTGTGGGTGTGTGGGTGTGTGGACTCGATGGGGTGTGTGGCCGGTGTGTGGATGTGTGGCCTGTGTGGTGTGTGGTGGTGTGTGGTATACCGGCTGAAGTGTGTGGTTGTGTGGTGTGTGGTGTGTGGTGTGTGGCGGTGTGTGGACTGTGTGTGGCTGTGTGGATGTGTGGGTGTGTGGAATGTGTGGTCGGCCCTGTGTGGGCATGTGTGGCCCTGTGTGGCCTGTGTGGAGTGTGTGGTGTGTGGCATGTGTGGTAATTGTGTGGTAGGAATGTGTGGCCACGTGTGTGGTCGTGTGTGGTGTGTGGTGCCGTGTGTGGCCTCGTAGTAGTGTGTGGGGGTATTTGTGTGGTGTGTGGGTGTGTGGTGTGTGGTGTGTGGATGTGTGGTGTGTGGGTGTGTGGTGTGTGGCTGTGTGGCACTGTGTGGCTCTTGACTCTATTGTGTGGACTGTGTGGTGTGTGGTGGTGTGTGGTTGTGTGGGTGTGTGGTGTGTGGAATGTGTGGGGTGTGTGGTTGTGTGGTAACTGCGCAGGTCTGACTGTGTGGTTCAGATGTGTGGCTGTGTGGAGGGATTAGTGTGTGGTGTGTGGTGTGTGGT"
    motif = "TGTGTGGTG"
    loc = findMotif(seq, motif)
    print(" ".join(loc))
