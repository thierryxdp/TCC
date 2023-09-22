def repetidos(lista):
    '''funçao que dada uma lista retorna o numero de vezes que um elemnto
    da lista é igual ao anterior'''
    indice = 0
    contador = 0
    while indice-1 < len(lista):
        if lista[indice] == lista[indice+1]:
            contador+=1
        indice += 1
    return contador