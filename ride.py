"""
ID: ben.wag1
LANG: PYTHON3
PROG: ride
"""
alphabet = {
	"A" : 1,
	"B" : 2,
	"C" : 3,
	"D" : 4,
	"E" : 5,
	"F" : 6,
	"G" : 7,
	"H" : 8,
	"I" : 9,
	"J" : 10,
	"K" : 11,
	"L" : 12,
	"M" : 13,
	"N" : 14,
	"O" : 15,
	"P" : 16,
	"Q" : 17,
	"R" : 18,
	"S" : 19,
	"T" : 20,
	"U" : 21,
	"V" : 22,
	"W" : 23,
	"X" : 24,
	"Y" : 25,
	"Z" : 26 }

#Receive User Input (six character string)
fin = open('ride.in', 'r')
fout = open('ride.out', 'w')

comet_name = fin.readline().upper().strip()
comet_value = 1

group_name = fin.readline().upper().strip()
group_value = 1

#Multiply character alphabet values together and mod 47
for i in range(len(comet_name)):
	comet_value *= alphabet[comet_name[i]]

for i in range(len(group_name)):
	group_value *= alphabet[group_name[i]]

comet_value = comet_value % 47
group_value = group_value % 47

if(comet_value == group_value):
	fout.write("GO\n")
else:
	fout.write("STAY\n")

fin.close()
fout.close()

"""
Solution Analysis:
	-My manual char_to_num alphabet hash table works but was inelegant.
	The following is a function which accomplishes the same thing with only two lines of code. (even smaller but less modular if you don't define a function)
	def char_to_num(c):
		return ord(c) - ord('A') + 1

	-I don't have to do range(len(str_name)) to iterate through the characters of a string. You can literally just do 
		for c in str_name: 
	
	-You can use 
		with open('ride.out', 'w') as fout:
	the with construct to automatically close file upon block exit.
"""