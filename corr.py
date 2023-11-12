#revc

def reverse_complement(sequence3):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp = [complement[base] for base in reversed(sequence3)]
    return ''.join(reverse_comp)

#hamm
def calculate_hamming_distance(s, t):
    if len(s) != len(t):
        raise ValueError("Input strings must be of equal length")
    
    hamming_distance = 0
    
    for i in range(len(s)):
        if s[i] != t[i]:
            hamming_distance += 1

    return hamming_distance

from Bio import SeqIO
from Bio import SeqIO
from Bio.Seq import Seq
from numpy import hamming

dna_strings = []
with open("rosalind_corr.txt", "r") as file:
    dna_string = ""
    for line in file:
        if line.startswith(">"):
            if dna_string:
                dna_strings.append(dna_string)
            dna_string = ""
        else:
            dna_string += line.strip()
    if dna_string:
        dna_strings.append(dna_string)

#print(dna_strings)

from Bio.Seq import Seq

corrections = []
correct_read= []

for element in dna_strings:
    if dna_strings.count(element) != 1 or dna_strings.count(reverse_complement(element)) == 1 : # present 2 times:or present as a reverse complement
        correct_read.append(element)
        continue#correct move one
    if dna_strings.count(element) == 1 and dna_strings.count(reverse_complement(element)) == 0: #present exactly one time
        for i in range(len(dna_strings)):
            hamm_distance = calculate_hamming_distance(element,dna_strings[i]) 
            hamm_distance_2 = calculate_hamming_distance(element,reverse_complement(dna_strings[i]))  #check hamm distaznce with dna_strings and their reverses
            if hamm_distance_2 ==  1 :
                corrected_read_2=reverse_complement(dna_strings[i])
                corrections.append(f"{element}->{corrected_read_2}")
                break
            if hamm_distance == 1 : 
                corrected_read = dna_strings[i] 
                corrections.append(f"{element}->{corrected_read}")
                break
             #correct and add to list of corrections--> corrections.append(f"{read}->{correct_read}")

#print(correct_read)
print(corrections)

