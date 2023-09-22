def faltante(lis):
    i = 0
    posi = 0
    fim == False
	lista = list(range(len(lis) + 1))
    lista.remove(0)
    while(i<len(lis) or fim == True):
        if(lis[i] == lista[i]):
            posi = lis[i] + 1
            i += 1
        else:
            posi = lista[i]
            i += 1
            fim == True
            
    return posi