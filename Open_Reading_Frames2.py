import re

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}


def fastaParser(bestand):
	"""Parse FASTA file, return sequence as string"""
	sequence = []
	with open(bestand) as inFile:
		for line in inFile:
			if not line.startswith(">"):
				sequence.append(line.strip())
	seq = "".join(sequence)
	return seq


def readingFrames(seq):
	"""Save the six reading frames in separate lists"""
	rev_seq = reverseStrand(seq)
	f1 = []
	f2 = []
	f3 = []
	r1 = []
	r2 = []
	r3 = []
	for i in range(0, len(seq), 3):
		if len(seq[i:i+3]) == 3:
			f1.append(seq[i:i+3])
		if len(seq[i+1:i+4]) == 3:
			f2.append(seq[i+1:i+4])
		if len(seq[i+2:i+5]) == 3:
			f3.append(seq[i+2:i+5])
		if len(rev_seq[i:i+3]) == 3:
			r1.append(rev_seq[i:i+3])
		if len(rev_seq[i+1:i+4]) == 3:
			r2.append(rev_seq[i+1:i+4])
		if len(rev_seq[i+2:i+5]) == 3:
			r3.append(rev_seq[i+2:i+5])
	readingframes = [f1, f2, f3, r1, r2, r3]
	return readingframes


def reverseStrand(seq):
	"""Make the forward strand reverse, return reverse-complementare
	 strand
	 """
	reverse = []
	for i in seq:
		if i == "A":
			reverse.append("T")
		if i == "T":
			reverse.append("A")
		if i == "C":
			reverse.append("G")
		if i == "G":
			reverse.append("C")
	return "".join(reversed("".join(reverse)))


def translate(seq):
	"""Translate the sequence into protein"""
	translated = []
	for s in seq: 
		temp = []
		for triplet in s: 
			temp.append(gencode[triplet])
		translated.append("".join(temp))
	return translated


def findORFs(trans_rf):
	"""Find open reading frames with regular expression"""
	orfs = []
	pattern = re.compile(r'(?=(M(?:.)*?)(?=_))')
	for seq in trans_rf:
		#x = re.search(regex, seq)
		for m in re.findall(pattern, seq):
			if m not in orfs:
				orfs.append(m)
	return orfs


if __name__ == "__main__":
	bestand = "rosalind_orf.txt"
	seq = fastaParser(bestand)
	readingframes = readingFrames(seq)
	translated_readingframes = translate(readingframes)
	orfs = findORFs(translated_readingframes)

	# Print the open reading frames
	for o in orfs:
		print(o)

