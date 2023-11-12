
import sys
from Bio import Phylo
import io

f = open('rosalind_nkew.txt', 'r')# read the content of the file
pairs = [i.split('\n') for i in f.read().strip().split('\n\n')]# assuming the file is organized into pairs separated by two newline characters.
#Each element in the pairs list is a string representing a pair.
for i, line in pairs:
    x, y = line.split()#This line splits the 'line' (the pair of nodes) into two values, 'x' and 'y', using whitespace as the delimiter
    tree = Phylo.read(io.StringIO(i), 'newick')# 'i' string contains a valid Newick format representation of a phylogenetic tree.
    sys.stdout.write('%s' % round(tree.distance(x,y)) + ' ')
sys.stdout.write('\n')


