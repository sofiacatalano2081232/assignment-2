from Bio import SeqIO

def read_fasta(filename):
    sequences = {}
    for record in SeqIO.parse(filename, "fasta"):
        sequences[record.id] = str(record.seq)
    return sequences

def find_overlap(s1, s2, k):
    return s1[-k:] == s2[:k]

def create_overlap_graph(fasta_file, k):
    sequences = read_fasta(fasta_file)
    adjacency_list = []

    for label1, seq1 in sequences.items():
        for label2, seq2 in sequences.items():
            if label1 != label2 and find_overlap(seq1, seq2, k):
                adjacency_list.append((label1, label2))

    return adjacency_list


fasta_file = "rosalind_grph.txt"
k = 3
adjacency_list = create_overlap_graph(fasta_file, k)

# Print the adjacency list
for edge in adjacency_list:
    print(f"{edge[0]} {edge[1]}")
