def maiores(lista, n):
    l = lista[:]    
    l.append(n)
    l1 = l[:]    
    list.sort(l1)
    l2 = l1[:]      
    i =list.index(l2,n)+1
    l3 = l2[i:]   
    return l3