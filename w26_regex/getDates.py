import re

dates = []

fh = open(r"datefile.dat","r").read()

patterns = [
    r"(?P<month>\d{1,2})+(\/|-)+(?P<day>\d{1,2})+(\/|-)+(?P<year>\d{4}|\d{2})+(\b)",
    r"(\b)+(?<!\/|-)+(?P<month>\d{1,2})+(\/|-)+(?P<year>\d{4})+(\b)",
    r"(?P<day>\d{2})+( )+(?P<month>Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)+( )+(?P<year>\d{4}|\d{2})+(\b)",
    r"(?P<month>Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)+(.|)+ (?P<day>\d{2})+[\s|,\s]+(?P<year>\d{4}|\d{2})+(\b)",
    r"(?P<month>Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)+( )(?P<year>\d{4})(\b)"
]

#P tags --> signals that the group is tagged by a certain name

for pattern in patterns:
    dates.append(re.findall(pattern,fh))

counter = 0
for d in range(len(dates)):
    for i in dates[d]:
        print(i)
        counter +=1
print(str(counter)+' dates found')
