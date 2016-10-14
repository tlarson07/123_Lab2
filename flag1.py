#opens file "hidden_in_plain_sight"
f = open ("hidden_in_plain_sight.txt")
#Puts the plain text from the file inside of a variable named content and allows us to read it
content = f.readline()
#finds the location of flag and stores it in the variable locatoin
location = content.find("flag")
#finds the location of } and stores it in the variable location2
location2 = content.find("}") + 1
#prints from location to location2
print content[location:location2 ]
