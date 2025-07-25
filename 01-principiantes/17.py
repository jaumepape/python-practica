L1 = [9, 8, 7, 14, 3, 2, "a", "p", "hola", "b"]
L2 = ["b", 1, 9.2, 6, 3, 9, "p"]

L3 = set(L2).intersection(set(L1))
L3 = list(L3)
print (L3)