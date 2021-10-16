import operator


def fastaParser(bestand):
    """Parse FASTA bestand to dictionary, return {header: seq, n}"""
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


def calcGC(seqs):
    """Calculate GC percentage"""
    percentages = {}
    for key, value in seqs.items():
        G = value.count("G")
        C = value.count("C")
        percentage = (G+C)/len(value)
        percentages[key] = round(percentage*100, 5)
    return percentages


def maxGC(percentages):
    """Get the maximum percentage and corresponding header"""
    max_percentage = max(percentages.items(), key=operator.itemgetter(1))[0]
    print(max_percentage)
    print(percentages[max_percentage])


if __name__ == "__main__":
    bestand = "computing_gc_content.txt"
    seqs = fastaParser(bestand)
    percentages = calcGC(seqs)
    maxGC(percentages)
