
with open("rosalind_tree (2).txt", "r") as file:
        lines = file.readlines()#-->each line is an edge
n =int(lines[0]) #first line is number of nodes
edges= len(lines[1:])       #all the other all the edges
result= n -1- edges #formula

print(result)


