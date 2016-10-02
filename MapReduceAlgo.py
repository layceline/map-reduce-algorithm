def map(line):
	line = line.replace(',', '')
	#Replace all punctuation
	words = line.split()
	mapper = []
	for word in words:
		item = (word, 1)
		mapper.append(item)
	#To remove later
	print(mapper)

#def shuffleAndSort():

#def reduce():

def main():
	file = open("test.txt", "r")
	lines = file.readlines()
	file.close()
	for line in lines:
		map(line)

main()