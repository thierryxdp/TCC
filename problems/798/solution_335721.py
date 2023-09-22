def freq_palavras (lista):
   
    rep = 0
    i = 0
    lista2=[]
    
    for i in range (len(lista)-1):
        if lista[i] == (lista[i+1]): 
            rep = rep + 1
        i = i + 1
        lista2=[(rep,lista[i])]
        dicionario = dict((y, x) for x, y in lista2)
    return lista2