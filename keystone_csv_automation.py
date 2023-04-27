#Import libraries and pull csv data from files.
import numpy as np
import pandas as pd

student_logins = pd.read_csv('./student_logins.csv', header=4)
keystone_data = pd.read_csv('./keystone_spreadsheet.csv')
grade_to_grad_year = {12 : 23, 11 : 24, 10 : 25, 9 : 26}


#Below pulls passwords from student spreadsheet and populates keystone spreadsheet.
for x, i in enumerate(keystone_data['User Name']):
	stu_index = student_logins[student_logins['User name'] == i].index.values
	if(student_logins['Password'].iloc[stu_index].values.size != 0):
		keystone_data.loc[x, 'Password'] = student_logins['Password'].iloc[stu_index].values[-1]


#Below combines 3 course columns into one single one. Might be a more elegant solution but whatever, this works.
for x in keystone_data.index:
	if(isinstance(keystone_data.loc[x, 'Algebra '], str)):
		if(isinstance(keystone_data.loc[x, 'Biology '], str)):
			if(isinstance(keystone_data.loc[x, 'Literature'], str)):
				keystone_data.loc[x, 'Courses'] = 'Algebra, Biology and Literature'
			else:
				keystone_data.loc[x, 'Courses'] = 'Algebra and Biology'
		elif(isinstance(keystone_data.loc[x, 'Literature'], str)):
			keystone_data.loc[x, 'Courses'] = 'Algebra and Literature'
		else:
			keystone_data.loc[x, 'Courses'] = 'Algebra'
	elif(isinstance(keystone_data.loc[x, 'Biology '], str)):
		if(isinstance(keystone_data.loc[x, 'Literature'], str)):
			keystone_data.loc[x, 'Courses'] = 'Biology and Literature'
		else:
			keystone_data.loc[x, 'Courses'] = 'Biology'
	elif(isinstance(keystone_data.loc[x, 'Literature'], str)):
		keystone_data.loc[x, 'Courses'] = 'Literature'
	else:
		keystone_data.loc[x, 'Courses'] = 'None'


#Now generate e-mails.
for x in keystone_data.index:
	#Grab first names, last names, grade level and student id.
	if(keystone_data.loc[x, 'First Name'] != 'EDGE_CASE'):
		stu_fname = student_logins.loc[student_logins[student_logins['User name'] == keystone_data.loc[x, 'User Name']].index.values, 'First Name'].values[-1]
		stu_lname = student_logins.loc[student_logins[student_logins['User name'] == keystone_data.loc[x, 'User Name']].index.values, 'Last Name'].values[-1]
		stu_grade = student_logins.loc[student_logins[student_logins['User name'] == keystone_data.loc[x, 'User Name']].index.values, 'Grade'].values[-1]
		stu_id = student_logins.loc[student_logins[student_logins['User name'] == keystone_data.loc[x, 'User Name']].index.values, 'Student Id'].values[-1]
		stu_id = str(stu_id)[-2] + str(stu_id)[-1]
		stu_email = str(grade_to_grad_year[stu_grade]) + stu_fname[0] + stu_lname + str(stu_id) + '@EMAIL_DEPRECATED.org'
	else:
		#Edge case. NAME DEPRECATED FOR SECURITY PURPOSES.
		stu_email = 'EMAIL@DEPRECATED.org'
	keystone_data.loc[x, 'E-Mail'] = stu_email


#Now output to file, go through and manually fix anomaly e-mails (hyphenated names, long names) to match proper format.
print(keystone_data)
keystone_data.to_csv('./updated_keystone_data.csv')