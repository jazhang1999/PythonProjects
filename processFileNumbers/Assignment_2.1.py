import re
#test text was renamed textSample.txt, while actual text was renamed textActual.txt
#handle = open('textSample.txt') - test before submitting
handle = open('textActual.txt')

masterList = []
for line in handle:
    numsInLine = re.findall('[0-9]+', line)
    masterList = masterList + numsInLine
    numsInLine = []

grandSum = 0
for number in masterList:
    grandSum = grandSum + int(number)
print("All Done")

#Find the answer, and check to see all numerical values are accounted for
print(grandSum)
print(len(masterList))
