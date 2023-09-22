def maiores(lista, n):
    l=[]
    i=0
    while lista[i]>n:
        l.append(i)
        i= i+1
        l.sort()
        
        return l