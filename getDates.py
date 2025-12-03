import re

dates = []

fh = open(r"datefile.dat","r").read()

patterns = [
    r"(?P<month>\d{1,2})+(\/|-)+(?P<day>\d{1,2})+(\/|-)+(?P<year>\d{4}|\d{2})+(\b)",
    r"(\b)+(?<!\/|-)+(?P<month>\d{1,2})+(\/|-)+(?P<year>\d{4})+(\b)",
    r"(?P<day>\d{2})+( )+(?P<month>January|Jan|February|Feb|Mar|March|Apr|April|May|Jun|June|July|Jul|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)+( )+(?P<year>\d{4}|\d{2})+(\b)",
    r"(?P<month>January|Jan|February|Feb|Mar|March|Apr|April|May|Jun|June|July|Jul|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)+(.|)+ (?P<day>\d{2})+[\s|,\s]+(?P<year>\d{4}|\d{2})+(\b)",
    r"(?P<month>January|Jan|February|Feb|Mar|March|Apr|April|May|Jun|June|July|Jul|Aug|August|Sep|September|Oct|October|Nov|November|Dec|December)+( )(?P<year>\d{4})(\b)"
]

for pattern in patterns:
    dates.append(re.findall(pattern,fh))

counter = 0
for d in range(len(dates)):
    for i in dates[d]:
        print(i)
        counter +=1
print(str(counter)+' dates found')