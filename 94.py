#open file
handle = open('mbox-short.txt')

#assign name to dictionary
counts = dict()

#read through file
for line in handle:
	#split the line so its a list
	line = line.rstrip()
	words = line.split()
	#identify only those lines/lists starting with From
	if len(words) < 1:
		continue
	if words[0] == 'From':
		#add the second word of this list to a dictionary and count 
		sender = words[1]
		if sender in counts:
			counts[sender] = counts[sender] + 1
		else:
			counts[sender] = 1
			#print('***NEW***')
		#print(sender,counts[sender])

#find the sender with the highest count

#define variables
bigSender = None
bigCount = None

#for each key pair in dictionary 
for sender,count in counts.items():
	#make sender bigSender if they have the most counts
	if bigSender is None or count > bigCount:
		bigSender = sender
		bigCount = count

print(bigSender, bigCount)