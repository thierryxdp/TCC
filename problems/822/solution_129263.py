def repetidos(lista):
    '''Função que retorna o numero de vezes que um item de uma lista é igual ao anterior
    entrada-lista
    saída-int'''
    i=0
    resultado=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
                resultado=resultado+1
        i=i+1
    return resultado