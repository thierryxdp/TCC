def maiores(lista, n):
    
    l_final = []
    
    for i in lista:
        if i > n:
            l_final.append(i)
            
    l_final.sort()
           
    return l_final