import re


def sumNums(fileName):
    """ prints sum of the numbers using a regex

        fileName - the name of the file to read from
    """
    sum = 0
   	
    # open the file for reading
    hand = open(fileName)

    # loop through the lines
    for line in hand:

    	# extract number
        numbers = re.findall('[0-9]+', line)

        # sum the numbers
        if not numbers:
        	continue
        else:
        	for number in numbers:
        		sum += int(number)
    return sum



def countWord(fileName, word):

    count = 0

    # open the file for reading
    hand = open(fileName)
    hand2 = hand.readlines()

    # loop through the lines
    for line in hand2:

        # find all words
        finded = re.findall(word+'\\b', line, re.IGNORECASE)
        
        count += len(finded)
		
    return count


def listURLs(fileName):

    # open the file for reading
    hand = open(fileName)


    # email list
    URList = []

    # loop through the lines
    for line in hand:

        # remove white space on the right side
        line = line.rstrip()

        # find all that start with a non space then @ then more non space
        currList = re.findall('www.[a-zA-Z0-9.-]+', line)


        # add the current list to the list of all
        URList += currList

    # return the number found
    return URList






print(sumNums('actual.txt'))
print(countWord('actual.txt', "computer"))
print(listURLs('regex_sum_42.txt'))


