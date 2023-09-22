def maiores(lista, n):
    def maiores(lista, n):
    l = lista[:]    
    l.append(n)
    l1 = l[:]
    
    list.sort(l1)
    l2 = l1[:]   
    
    n =list.index(l2,n)   
    l3 = l2[n:]
    
    return l3