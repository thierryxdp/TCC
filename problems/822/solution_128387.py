def repetidos(lista):
    '''função em que dada uma lista de números, retorna
    o número de vezes que um elemento da lista é igual
    ao elemento anterior; list -> list'''
    repet = []
    n = 0
    for i in range(0, len(lista)):
        n = 0
        for x in range (i, len(lista)):
            if(lista[i] == lista[x]):
                n += 1
        if(n > 1):
            
            if (repet == []):
                repet.append(lista[i])
            else:
                dup = 0
                for j in range(0, len(repet)):
                    if(lista[i] == repet[j]):
                        dup +=1
                if (dup < 1):        
                    repet.append(lista[i])
    return repet