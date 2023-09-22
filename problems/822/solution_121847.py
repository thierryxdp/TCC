def repetidos(lista):
    '''Função que recebe de entrada um lista de numeros e retorna o numero
    de vezes que um elemento da lista e igual ao anterior.list->int'''
    i=1
    total=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            total=total+1
        i=i+1
    return total