def repetidos(lista):
    ''' funcao que apos ser dada uma lista composta por numeros
    ela retornara a quantidade de itens repetidos nesta lista.
    list -> int '''
    i=0
    repeticoes = 0
    
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            repeticoes = repeticoes + 1
        i = i+1
    return repeticoes