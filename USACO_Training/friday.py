"""
ID: ben.wag1
LANG: PYTHON3
PROG: friday
"""
import os

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] #[] ordered list, {} set
weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
thirty = {"September", "April", "June", "November"}
thirtyOne = {"January", "March", "May", "July", "August", "October", "December"}
#February has 28 days, except on leap years when it has 29. 
#A Leap year occurs when the year is divisible by 4, centuries must be divisible by 400 (2000, not 1900 or 2100)
day0 = "January 1, 1900 Monday"
counter = {"Saturday": 0, "Sunday": 0, "Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0}

fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

years = fin.readline().strip()

def getWeekday(currentDay):
	return currentDay.split()[3]

def getDay(currentDay):
	return currentDay.split()[1].split(',')[0]

def nextDay(currentDay):
	x = currentDay.split()
	currentMonth = x[0]
	day = x[1].split(',')[0]
	currentYear = x[2]
	currentWeekday = x[3]
	nextWeekday = ""

	if(currentWeekday == "Friday"):
		nextWeekday = "Saturday"
	else:
		nextWeekday = weekdays[weekdays.index(currentWeekday) + 1]

	if(currentMonth in thirtyOne):
		if(int(day) == 31):
			#iterate month, year if necessary
			if(currentMonth == "December"):
				return "January 1, " + str(int(currentYear) + 1) + " " + nextWeekday
			else:
				return months[months.index(currentMonth) + 1] + " " + str(1) + ", " + currentYear + " " + nextWeekday
		else:
			return currentMonth + " " + str(int(day) + 1) + ", " + currentYear + " " + nextWeekday
	elif(currentMonth in thirty):
		if(int(day) == 30):
			return months[months.index(currentMonth) + 1] + " " + str(1) + ", " + currentYear + " " + nextWeekday
		else:
			return currentMonth + " " + str(int(day) + 1) + ", " + currentYear + " " + nextWeekday
	else:
		#February
		if((int(currentYear) % 100 ) == 0):
			if((int(currentYear) % 400) == 0):
				#Century Leap Year such as the year 2000
				if(int(day) == 29):
					return months[months.index(currentMonth) + 1] + " " + str(1) + ", " + currentYear + " " + nextWeekday
				else:
					return currentMonth + " " + str(int(day) + 1) + ", " + currentYear + " " + nextWeekday
			else:
				#not a leap year
				if(int(day) == 28):
					return months[months.index(currentMonth) + 1] + " " + str(1) + ", " + currentYear + " " + nextWeekday
				else:
					return currentMonth + " " + str(int(day) + 1) + ", " + currentYear + " " + nextWeekday
		elif((int(currentYear) % 4) == 0):
			#leap year
			if(int(day) == 29):
				return months[months.index(currentMonth) + 1] + " " + str(1) + ", " + currentYear + " " + nextWeekday
			else:
				return currentMonth + " " + str(int(day) + 1) + ", " + currentYear + " " + nextWeekday
		else:
			#not a leap year
			if(int(day) == 28):
				return months[months.index(currentMonth) + 1] + " " + str(1) + ", " + currentYear + " " + nextWeekday
			else:
				return currentMonth + " " + str(int(day) + 1) + ", " + currentYear + " " + nextWeekday

currentDay = day0

#count leap years
leaps = 0
for i in range(int(years)):
	if(((1900 + i) % 100) == 0):
		if(((1900 + i) % 400) == 0):
			leaps = leaps + 1
	elif(((1900 + i) % 4) == 0):
		leaps = leaps + 1

for i in range(int(years)*365 + leaps):
	if(int(getDay(currentDay)) == 13):
		counter.update({getWeekday(currentDay): (int(counter.get(getWeekday(currentDay))) + 1)})
	currentDay = nextDay(currentDay)

counter2 = 0
for value in counter.values():
	if(counter2 < 6):
		fout.write(f'{value} ')
	else:
		fout.write(f'{value}\n')
	counter2 = counter2 + 1

fin.close()
fout.close()

"""
Sean Gao's simple solution:

def is_leap_year(year):
    ret = False
    if year % 100 == 0:
        ret = year % 400 == 0
    else:
        ret = year % 4 == 0
    return ret

with open ('friday.in', 'r') as fin:
    raw_line = fin.readline()
years = int(raw_line.strip())

weekdays = [0] * 7
days_of_months = [31,28,31,30,31,30,31,31,30,31,30,31]

curr_days = 0
for year in range(1900, 1900+years):
    for month in range(12):
        _13th = 13 + curr_days
        weekday = _13th % 7
        mon = month+1
        weekdays[weekday] += 1
        curr_days += days_of_months[month]
        if month == 1 and is_leap_year(year):
            curr_days += 1
output = str(weekdays[6])	# task wants specific order
for n in range(6):
    output += ' ' + str(weekdays[n])
with open ('friday.out', 'w') as fout:
    fout.write(output + '\n')

ANALYSIS:
	I took a completely different route than Sean Gao did here, and that is okay!
		My code could definitely be more streamlined but I am happy with my results.
		I definitely did not have to create a system for writing out each individual date, then filter through the iteration of such a system to get the results.
		This was merely to make the task of creation easier for me so I could see exactly what the program was doing as I created it.
		Sean Gao takes a more calculation-based approach. I avoided this route by prioritizing accuracy before anything else with my systemic approach. This is more modular and 
		could more easily be expanded to a larger program, however for the purpose of a coding challenge looks quite a bit clunky.

	In the future, experiment with these sort of "shortcut" calculation type answers. Embrace being wrong and see where it takes you. Sometimes 
		this touch of chaos can be a gateway to creativity.
"""