def repetidos(num):
    """essa função recebe uma lista e retorna o número de vezes que um elemento da lista sucede ele mesmo;
    list->int"""
    i = 1
    lista = []
    while i<len(num):
        if num[i] == num[i-1]:
            lista==[lista,num[i]]
            i == 1
    return len(lista)/2