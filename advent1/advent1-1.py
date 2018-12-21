
curr = 0

file = open("string.txt","r")
#iterate through every line in file
for line in file:
    mult = 1
    absDelta = int(line[1:len(line)])
    
    #get pos/neg
    if line[0] == '-':
        mult = -1
        
    delta = absDelta * mult 
    curr += delta
    
file.close()

print(curr)


