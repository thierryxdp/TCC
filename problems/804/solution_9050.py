def filtra_pares (n):
    list1 = [n]
    list2 = []
    for valor in list1:
        if valor%2 == 0:
            list2.append(valor)
            
    return list2
        
print (filtra_pares (n))