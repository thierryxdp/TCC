def filtra_pares (a, b, c, d):
    list1 = [a, b, c, d]
    list2 = []
    for [a, b, c, d] in list1:
        if [a, b, c, d]%2 == 0:
            list2.append(a, b, c, d)
            
    return list2
        
print (filtra_pares (a, b, c, d))