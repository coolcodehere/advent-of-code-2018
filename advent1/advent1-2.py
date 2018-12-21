
curr = 0
checkSet = set()
loop = True
checkSet.add(curr)

while loop:
    file = open("string.txt","r")
    #iterate through every line in file
    for line in file:
        mult = 1
        absDelta = int(line[1:len(line)])
        
        #get pos/neg
        if line[0] == '-':
            mult = -1
        delta = absDelta * mult 
        
        #add the delta
        curr += delta
        
        #check if frequency in set
        if curr in checkSet:
            print(curr)
            loop = False
            break
        else:
            checkSet.add(curr)
    file.close()


