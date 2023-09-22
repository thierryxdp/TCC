def conta_numero(n,lista):
    
    
    i=0
    y=len(lista)
    contador=0
    
    while i<y:
        contador+=lista[i].count(n)
        i+=1
    return contador