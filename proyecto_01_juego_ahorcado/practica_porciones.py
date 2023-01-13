# Basico con listas
l1 = ['O','S','I','T','O']
l2 = ['O','S','I','T']
l3 = [i if i in l2 else '-' for i in l1]

print(set(l1) == set(l2))

# for i in l3: 
#     print(i,end=' ')