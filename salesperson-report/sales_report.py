"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] #Create an empty list for name of salesperson
melons_sold = [] #Create an empty list for # of melons sold

f = open('sales-report.txt') #open sales-report text file
for line in f: #loop through each line of the file
    line = line.rstrip() #strip the white space to the right
    entries = line.split('|') #create a list of entries by line split by | 

    salesperson = entries[0] #name of person is the 0 index of the list
    melons = int(entries[2]) #number of melons is the 2nd index of the list
    #convert it to an integer using int 

    if salesperson in salespeople: #if the person's name is in the list salespeople
        position = salespeople.index(salesperson) #the position of the person is the
        #index they are at in salespeople

        melons_sold[position] += melons #then at the same index of the melons_sold
        #list, add the melons on that line
    else:
        salespeople.append(salesperson) #if name not found in salespeople,
        #add the name to the end of the list
        melons_sold.append(melons) #add the melons sold to the end of the melons
        #list


for i in range(len(salespeople)): #for the length of the list at each index
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') #print how much the person sold
