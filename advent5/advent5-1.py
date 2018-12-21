file = open("input.txt","r")

string = ""
for line in file:
    string = line

print(len(string))
prev = ''
red = 0

for i in range(len(string)): 
    current = string[i-red].upper()

    if i-red > 0:
        prev = current

    if prev == current:
        string = string[:i-red-2] + string[i-red:]
        red += 1
      

print(len(string))
