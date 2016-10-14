#opens file one_plus_one_equals_flag.txt
f = open ("one_plus_one_equals_flag.txt")
#allows us to read the file
content = f.readline()
#start and count variables start at 0
start = 0
count = 0
#sets up flag as an empty string
flag = ""

#run loop until the location of content has reached "}"
while content [start]  != "}":
    #put character from content based on index from start + conunt in flag
    flag = flag + content[start + count]
    #keep track of where we are in the file by adding where we are currently plus the count
    start = start + count
    #increase count by one
    count = count + 1
print flag
