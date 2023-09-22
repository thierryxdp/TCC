def maiores(lista, n):
    l=[]
    i=0
    while lista[i]>n:
        l.append(i)
        i++
        l.sort()
        
        return l