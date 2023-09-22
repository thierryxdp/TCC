def faltante(l):
    
    maior=max(l)
    menor=min(l)
    i=0
    numeros=[]
    
    while i<len(l):
        if i!=maior and i!=menor and (i+1 not in l or i-1 not in l):
            return list.append(numeros,i)
        i=i+1