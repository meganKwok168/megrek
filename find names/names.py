import re

dates = []

fh = open(r"namefile3.dat","r").read()

namesFull = []
namesFound = []
patterns = []

#P tags --> signals that the group is tagged by a certain name

# for pattern in patterns:
#     dates.append(re.findall(pattern,fh))
#
# counter = 0
# for d in range(len(dates)):
#     for i in dates[d]:
#         print(i)
#         counter +=1
# print(str(counter)+' dates found')
patterns = [r'^([A-Z]| |Á|É)([a-z]|.)([A-Za-z]|.)*\n']

namesFull.append(re.findall(patterns[0],fh))

print(namesFull)
