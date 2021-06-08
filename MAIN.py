import random

lowerCase="abcdefghijklmnopqrstuvwxyz"
upperCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
specialSymbols="[]{}()-;/,._-<>"

addAll=lowerCase+upperCase+numbers+specialSymbols
length=12
password="".join(random.sample(addAll,length))
print(password)