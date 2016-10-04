def map(line):
	words = line.split()
	mapper = []
	for word in words:
		item = (word, 1)
		mapper.append(item)
	return mapper

def shuffleAndSort(mappedWords):
	#sort alphabetically
	sortedList = sorted(mappedWords, key=lambda mappedWords: mappedWords[0].lower())
	
	factorizedList = []
	occurences = 1
	count=0
	while count != len(sortedList)-1:
		if sortedList[count][0]==sortedList[count+1][0]:
			occurences = occurences + 1
		else:
			if occurences == 1:
				factorizedList.append(sortedList[count])
			else:
				iteration = []
				for j in range (0, occurences):
					iteration.append(1)
				tup = (sortedList[count][0], iteration)
				factorizedList.append(tup)
				occurences = 1
		count = count + 1

	return factorizedList

def reduce(shuffled):
	reduced = []
	for tup in shuffled:
		if tup[1] == 1:
			reduced.append(tup)
		else:
			item = (tup[0],len(tup[1]))
			reduced.append(item)
	return reduced

def main():
	punctuations = ['@','#','&','"','(',')','§','!','[',']','{','}',',','?','.',';',':','/','<','>','+','=','-','_']
	#Open the file to count words from
	file = open("test.txt", "r")
	#Split the text into lines and put them in a list (Input Reader)
	lines = file.readlines()
	#Close the file
	file.close()

	mapped = []
	for line in lines:
		for character in line:
			if character in punctuations:
				line = line.replace(character, '')
		mapped.extend(map(line))

	shuffledTuples = shuffleAndSort(mapped)
	output = reduce(shuffledTuples)
	print(output)

main()