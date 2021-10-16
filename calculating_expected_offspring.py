
def readData(filenaam):
	"""Read file into list"""
	lijst = []
	with open(filenaam) as inFile:
		for line in inFile:
			lijst = line.split()
	return lijst


def calcOffspring(lijst):
	"""Calculate the expected offspring"""
	offspring = float(0)
	for i in range(len(lijst)):
		if i == 0 and lijst[0] != 0: 
			offspring += (float(lijst[i])*2)

		if i == 1 and lijst[1] != 0: 
			offspring += (float(lijst[i])*2)

		if i == 2 and lijst[2] != 0:
			offspring += (float(lijst[i])*2)

		if i == 3 and lijst[3] != 0:
			offspring += (float(lijst[i])*0.75)*2

		if i == 4 and lijst[4] != 0:
			offspring += (float(lijst[i])*0.5)*2

		if i == 5 and lijst[5] != 0:
			offspring += 0
		#print(offspring)
	print(offspring)


if __name__ == "__main__":
	file = "dataset_Calculating Expected Offspring.txt"
	#file = "rosalind_iev.txt"
	lijst = readData(file)
	calcOffspring(lijst)
# 1 AA-AA
# 2 AA-Aa
# 3 AA-aa
# 4 Aa-Aa
# 5 Aa-aa
# 6 aa-aa