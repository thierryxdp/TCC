def repetidos(lista):
    """Funcao que recebe uma lista de numeros e retorna o numero de vezes que um elemento da lista é igual ao anterior;list->str"""
    contagem=0
    i=0
    while i<len(lista)-1:
        if lista[i+1]=lista[i]:
            contagem=contagem+1
        i=i+1
    return contagem