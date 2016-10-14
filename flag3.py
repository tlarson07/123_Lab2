#opens file "quad-radical.txt"
f = open ("quad-radical.txt")
#allows us to read the file
content = f.readline()

#GENERALLY: variable that gives us the exact location of where we are in the string
#SPECIFICALLY: start at the index of 3
start = 3
#Count and inc variables start at 0
count = 0
inc = 0
#sets up flag as an empty string
flag = ""

#while start(where we are at in the file) is less than our content contiune loop
while start < len(content):
    #stores the indexs in flag
    flag = flag + content [start]
    #The coefficent by which our quadradic function increase by one
    inc = inc + 1
    #quadradic function
    count = (inc + 1)**2 +1
    #Adds the count to the start index
    start = start + count

#prints the first two charcters + the remaining portion using the equation
print content[0:2] + flag
