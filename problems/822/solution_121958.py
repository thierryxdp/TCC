def repetidos(lista):
    """Função que recebe uma lista e retorna o número de vezes que um elemento
    é igual ao anterior."""
    """list-->int"""
    i=0
    resultado=0
    while i,len(lista):
        if lista[i]==lista[i-1]:
            resultado=resultado+1
        i=i+1
    return resultado