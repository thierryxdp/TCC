def faltante(lis):
    i = 0
    posi = 0
	lista = list(range(len(lis + 1)))
    lista.remove(0)
    
    while(i<len(lis)):
        if(lis[i] == lista[i]):
            i += 1
            posi = lis[i] + 1
        else:
            posi = lis[i]
            
    return posi