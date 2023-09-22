def faltante (listanum):
    '''Função descobre qual número inteiro esta faltando em uma ordem crescente de 1 a N;
    list -> int'''
    indice = 0 
    list.sort (listanum)
    if listanum[indice] != 1:
        return 1 
    while indice != len (listanum) -1:
        if listanum[indice+1] != listanum[indice]+1:
            return listanum[indice]+1
    return int (listanum[-1]+1)
        indice = indice +1