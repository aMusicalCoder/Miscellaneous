"""
ID: ben.wag1
LANG: PYTHON3
PROG: gift1
"""
import os 

#Open Input/Output Streams

fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

"""
fin.seek(offset, whence=SEEK_SET) changes the stream position to the given byte offset. 
	Values of whence are:
		SEEK_SET or 0-start of stream, offset should be zero or positive.
		SEEK_CUR or 1-current stream position, offset may be negative.
		SEEK_END or 2-end of stream, offset is usually negative.

fin.tell() returns current stream position.
"""
#Find ending stream position of file.
fin.seek(0, os.SEEK_END)
end_pos = fin.tell()
fin.seek(0, os.SEEK_SET)

#Start reading data.

#Get number of members.
NP = fin.readline().strip() #line 1 is NP
members = {}

#populate list with member names.
for i in range(int(NP)):
	members.update({fin.readline().strip() : 0})

while(fin.tell() < end_pos):
	gift_giver = fin.readline()
	gift_data = fin.readline()

	amount_of_money = int(gift_data.split()[0])
	num_of_patrons = int(gift_data.split()[1])

	if(num_of_patrons != 0):
		cash_per_patron = int(amount_of_money/num_of_patrons)

		for i in range(num_of_patrons):
			patron_name = fin.readline().strip()
			current_balance = members[patron_name]
			members.update({patron_name : current_balance + cash_per_patron})

		#update giver's balance.
		current_giver_balance = members[gift_giver.strip()]
		remainder = amount_of_money % num_of_patrons
		members.update({gift_giver.strip() : (current_giver_balance - amount_of_money + remainder)})


#Output Final data. 
#f"{variable1} {variable2}" for string formatting.
for key in list(members.keys()):
	fout.write(f'{key} {members[key]}\n')

#Close I/O streams
fin.close()
fout.close()