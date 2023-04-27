import numpy as np 
import pandas as pd

df = pd.read_csv('./cb_remaining.csv')

df = df.melt().drop('variable', axis=1).dropna()
emails = df.squeeze()
emails.name = 'E-mail 1 - Value'

df2 = pd.read_csv('./email_import_template.csv')
df2 = df2.merge(emails, how='right') #edit so only specifically emails.name col 

for a in df2[emails.name].index:
	df2.at[a, emails.name] = df2.at[a, emails.name] + '@ADDRESS_DEPRECATED.org'

print(df2)
df2.to_csv('./for_gmail.csv')