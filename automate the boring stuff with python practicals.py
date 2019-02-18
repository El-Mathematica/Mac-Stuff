#Practicals from automate the boring stuff with python

#Chapter 7 - Regex

import re
#preceding command to required to import all regex functions in python


#passing a string value representing your regular expression to re.compile() returns a Regex pattern object

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #phonenumberregex contains a regex object
print(phoneNumberRegex)
