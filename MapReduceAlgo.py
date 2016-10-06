#Function that takes a line into paramter
#It will split the line into words, and create a tuple for each word, with a weight of 1
#Every tuple is put into the returned list
def map(line):
	#Split lines into words
	words = line.split()
	#Initialization of an empty array of mapped tuples
	mapper = []

	for word in words:
		#Creation of a tuple for each word of the line
		item = (word, 1)
		#Put the tuple in the mapper
		mapper.append(item)
	return mapper

#Function that takes the list of mapped words into paramater
#It will sort the list alphabetically
#It will append each tuple in a list and if it already exists, it will create a new tuple
#with a list of 1 that represents the number of appearences of this word
#For example, if the word "it" appears twice its tuple is ('it',[1,1])
def shuffleAndSort(mappedWords):
	#sort alphabetically
	sortedList = sorted(mappedWords, key=lambda mappedWords: mappedWords[0].lower())
	
	#Initialization of local variables
	factorizedList = []
	occurences = 1 #Number of occurence of a word in the whole text
	count=0 #Counter of tuple to 

	#While loop to compare every sorted tuples
	while count != len(sortedList)-1:
		#If a tuple is the same as the next one, I increment the number of occurence of the word
		if sortedList[count][0]==sortedList[count+1][0]:
			occurences = occurences + 1
		else:
			#If the word appears only once, I append it as it is in the factorizedList
			if occurences == 1:
				factorizedList.append(sortedList[count])
			#If the word appears more than once, I create a new tuple
			#This new tuple has the word and an array of 1 that represents the number of occurence
			#I append the new tuple to the factorizedList
			else:
				iteration = []
				for j in range (0, occurences):
					iteration.append(1)
				tup = (sortedList[count][0], iteration)
				factorizedList.append(tup)
				occurences = 1
		#Increment the counter to go through the list and exit the loop
		count = count + 1

	#Manage last tuple the same way I did the others 
	if occurences != 1:
		iteration = []
		for j in range (0, occurences):
			iteration.append(1)
		tup = (sortedList[count][0], iteration)
		factorizedList.append(tup)
		occurences = 1
	else:
		factorizedList.append(sortedList[count])

	return factorizedList

#This function takes the shuffled and sorted list of tuples as parameters
#It reduces the array of occurences to the number of occurences
#I chose to do it this way because I didn't know if I should separate the shuffleAndSort from the reduce
#These two functions could have easily been merged
#Instead of creating a new tuple with an array of 1, I could have directly created the tuple with the right number of occurences
def reduce(shuffled):
	reduced = []
	#For every tuple of the list, I check if the second value of the tuple 1 or not
	for tup in shuffled:
		#If it is, I append this tupple to the reduced list that I will return
		if tup[1] == 1:
			reduced.append(tup)
		#If it isn't, I create a new tuple with the word and its number of occurence
		else:
			item = (tup[0],len(tup[1]))
			reduced.append(item)
	return reduced

def mapReduce():
	#Characters to remove from the text before doing the mapping
	punctuations = ['@','#','&','"','(',')','§','!','[',']','{','}',',','?','.',';',':','/','<','>','+','=','-','_']
	#I did not manage the apostrophed words

	#Open the file to count words from
	file = open("text.txt", "r")
	#Split the text into lines and put them in a list (Input Reader)
	lines = file.readlines()
	#Close the file
	file.close()

	#Initialization of the table where each mapped lines will be stored
	mapped = []

	#For each line of the text
	for line in lines:
		#I am checking if each character is a punctuation symbol defined in punctuactions, if it is, I replace it
		for character in line:
			if character in punctuations:
				line = line.replace(character, '')
		#Then, I apply the map function to the line and put the result in an unique list called mapped
		mapped.extend(map(line))

	#I apply the shuffleAndSort function to the mapped lines
	shuffledTuples = shuffleAndSort(mapped)

	#Finally, I apply the reduce function to the shuffled and sorted tuples and print the result
	output = reduce(shuffledTuples)
	print(output)

mapReduce()