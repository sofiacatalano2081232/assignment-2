def count_internal_nodes(n):
    if n < 3:
        raise ValueError("n must be at least 3")
    return n - 2


n = 4751
  
internal_nodes = count_internal_nodes(n)
print(internal_nodes)
