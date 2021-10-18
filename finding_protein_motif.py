import urllib2
import re


def readRosalindFile(best):
	"""Return accession codes from Rosalind file"""
	acc = []
	with open(best) as inFile:
		for line in inFile:
			acc.append(line.strip())
	return acc


def createLink(acc_codes):
	"""Return a list with uniprot URLs"""
	links = []
	for i in acc_codes:
		link = "http://www.uniprot.org/uniprot/{}.fasta".format(i)
		links.append(link)
	return links


def readFasta(url):
	"""Return dictionary with fasta file: {header:seq}"""
	dictio = {}
	response = urllib2.urlopen(url)
	fasta = response.readlines()
	key = url.split("/")[-1].split(".")[0]
	for line in fasta: 
		line = line.strip()
		if line.startswith(">"):
			#key = line.split("|")[1]
			dictio[key] = []
		else:
			dictio[key].append(line)
	dictio = {key: "".join(value) for key, value in dictio.items()}
	return dictio


def retrieveFastas(links):
	"""Return list with dictionaries containing each FASTA file

	dictionaries = [{header: seq}, {header, seq}]
	"""
	dictionaries = []
	for i in links: 
		dictionaries.append(readFasta(i))
	return dictionaries		


def findMotif(fastas):
	"""Locate the motif in the sequences and save in dictionary matches"""
	matches = {}
	p = re.compile("N(?=[^P][ST][^P])")
	for entry in fastas:
		for m in p.finditer(entry.values()[0]):
			key = entry.keys()[0]
			if key not in matches:
				matches[key] = [str(m.start()+1)]
			else:
				matches[key].append(str(m.start()+1))
	return matches


if __name__ == "__main__":
	#rosalindBest = "finding_prot_motif.txt"
	rosalindBest = "rosalind_mprt.txt"
	# Collect the accession codes
	acc_codes = readRosalindFile(rosalindBest)
	# Create urls from Uniprot
	links = createLink(acc_codes)
	# Get all fastas with Uniprot URLs
	fastas = retrieveFastas(links)
	# Search with motif in sequences
	matches = findMotif(fastas)

	#output
	for key, value in matches.items():
		print (key)
		print (' '.join(value))
