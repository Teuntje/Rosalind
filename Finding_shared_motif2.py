
def readFile(bestand):
	"""Read fasta bestand into dictionary: {header: seq, n}, return only
	the values
	"""
	fastaDic = {}
	# Open and read the file
	with open(bestand) as inFile:
		for line in inFile:
			line = line.strip()
			# Creation of key and values
    		if line.startswith(">"):
				key = line.split(">")[1]
				fastaDic[key] = []
			else:
				fastaDic[key].append(line)
	# Values are all strings in lists, so they should be joined
	fastaDic = {key: "".join(value) for key, value in fastaDic.items()}
	return fastaDic.values()


def splitLists(fasta_list, steps):
	"""Split the fasta list into substrings and save these in de
	steps_list
	"""
	steps_list = []
	for i in fasta_list:
		steps_list.append(splitString(i, steps))
	return steps_list


def splitString(string, steps):
	"""Split the string into smaller sub strings"""
	lijst = []
	for i in range(len(string)):
		if len(string[i:i+steps]) == steps:
			lijst.append(string[i:i+steps])
	return set(lijst)


def findMotif(splitted_list, steps):
	"""Find a shared motif"""
	#print(set.intersection(*splitted_list))
	return set.intersection(*map(set,splitted_list))


if __name__ == "__main__":
	file = "finding_shared_motif.txt"
	#file = "rosalind_lcsm.txt"
	fasta_list = readFile(file)
	steps = 2
	while steps < len(sorted(fasta_list, key=len)[0]):
		splitted_list = splitLists(fasta_list, steps)
		#print(splitted_list)
		motif = findMotif(splitted_list, steps)
		if bool(motif):
			print(list(motif)[0])
		else:
			break
		steps += 1