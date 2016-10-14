#opens file "I_fibbed.txt"
f = open ("I_fibbed.txt")
#allows us to read the file
content = f.readline()
#all the vairables start at 0 except for y because you need to
x1 = 0
y1 = 1
x2 = 0
y2 = 0
start = 0
#sets up flag as an empty string
flag = ""

while content [start]  != "}":
    #x2 becomes x1
    x2 = x1
    #y2 becomes y1
    y2 = y1
    #x1 becomes y2
    x1 = y2
    #y1 becomes x2 added to y2
    y1 = x2 + y2
    #added the +1 as a phase shift to get the correct indexes
    start = start + x2 + 1
    #allows us to print everything on one line :D because we put each character in the variable flag
    flag = flag + content [start]
#heres the print for real
print content [0] + flag
