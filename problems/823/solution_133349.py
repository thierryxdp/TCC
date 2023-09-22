def faltante(lista):
    
    list.sort(lista)    
    indice = 0
    peca = 1
    
    while indice != len(lista) -1:
        if peca == lista[indice]:
            indice += 1
            peca =+ 1
        else:
            break
        
        if peca == lista[-1]:
            return peca
        else:
            return peca