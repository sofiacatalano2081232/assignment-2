
from Bio import SeqIO

#store sequences 
sequences = []
#open file
f = open('rosalind_long.txt', 'r')
#reading fasta format
for x in SeqIO.parse(f, 'fasta'):
    sequences.append(str(x.seq))

#store
solution = []
for y, z in enumerate(sequences):
  count = (len(z)+1)//2
  for k, j in enumerate(sequences):
    if y != k:
      match = j.find(z[-count:])
      if match >= 0 and z[-count-match:]==j[:count+match]:
        solution.append((y,k,count+match))

left = [x[0] for x in solution]
right = [x[1] for x in solution]
begin = set(left) - set(right)

#result string 
result = ""
fragment= list(begin)[0]
while True:
    result += sequences[fragment]
    x = [x for x in solution if x[0]==fragment]
    if x:
        fragment = x[0][1]
        result = result[:-x[0][2]]
    else:
        break

#print result 
print(result)