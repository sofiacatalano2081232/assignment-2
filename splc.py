from Bio import SeqIO
from Bio import SeqIO
from Bio.Seq import Seq

dna_strings = []
with open("rosalind_splc.txt", "r") as file:
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

#now we have a list with one string and two introns
string = dna_strings[0]

sliced_strings =[]
sliced_string = ''
for element in dna_strings[1:]:
    for  i in range(len(string)- len(element) + 1) :
        if string[i:i + len(element)] == element:
            sliced_string = string[:i] + string[i+len(element):]
            sliced_strings.append(sliced_string)
            string = sliced_strings[len(sliced_strings)-1]


#print(sliced_strings)
exon_sequence = sliced_strings[len(sliced_strings)-1]
#print(exon_sequence)

#now we transcribe
transcribed = ''
for symbol in exon_sequence:
     if symbol== 'T':
        transcribed+= 'U' #exchange T with U
     else:
        transcribed += symbol

#now we translate

# Define a dictionary that maps RNA codons to amino acids
codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}


protein = ''
for i in range(0, len(transcribed), 3):
    codon = transcribed[i:i+3] # from i position to i+3, we get the codon
    amino_acid = codon_table.get(codon, None)
    if amino_acid == 'Stop':
        break  # Stop codon indicates the end of translation
    if amino_acid:
        protein += amino_acid
    else:
        protein += 'X'  # Replace with 'X' if codon is unknown

print(protein)
