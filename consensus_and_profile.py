

def readFile(bestand):
    """Read fasta file into dictionary return {header: seq, n}"""
    fastaDic = {}
    #Open and read the file
    with open(bestand) as inFile:
        for line in inFile:
            line = line.strip()
            # Creation of key and values
            if line.startswith(">"):
                key = line
                fastaDic[key] = []
            else:
                fastaDic[key].append(line)
    #Values are all strings in lists, so they should be joined
    fastaDic = {key: "".join(value) for key, value in fastaDic.items()}

    return list(fastaDic.values())


def matrix(fastaParse):
    """Create a dictionary with counts for every position and append
    these counts to the corresponding nucleotide (key)

    :param fastaParse - dictionary {header: seq, n}
    return this dictionary with counts
    """
    positions = {"A" : [0]*(len(fastaParse[0])),
                 "C" : [0]*(len(fastaParse[0])),
                 "G" : [0]*(len(fastaParse[0])),
                 "T" : [0]*(len(fastaParse[0]))}
    for j in fastaParse:
        for i in range(len(fastaParse[0])):
            if j[i] == "A":
                positions["A"][i] += 1
            elif j[i] == "C":
                positions["C"][i] += 1
            elif j[i] == "G":
                positions["G"][i] += 1
            elif j[i] == "T":
                positions["T"][i] += 1
    return positions


def consensus(matrix):
    """Get the consensus pattern from the dictionary 'matrix'"""
    # Convert the keys and values separately into lists
    values = list(matrix.values())
    keys = list(matrix.keys())
    # Zip the values
    zip_values = list(zip(*values))
    consensus = ""

    # Check for every position within the zip values which value is the
    # highest, the next step is to get the index of the keys (so the
    # corresponding nucleotide)
    for i in range(len(zip_values)):
        index = zip_values[i].index(max(zip_values[i]))
        consensus += keys[index]
    return consensus


def prettyprint(matrix, consensus):
    """Pretty print the output"""
    print(consensus)
    
    for key, value in matrix.items():
        print(key + ": " + " ".join(str(x) for x in value))


if __name__ == "__main__":
    bestand = "rosalind_cons.txt"
    #bestand = "rosalind_consensus_and_profile.txt"
    fastaDic = readFile(bestand)
    positions = matrix(fastaDic)
    consensus = consensus(positions)
    prettyprint(positions, consensus)
    
