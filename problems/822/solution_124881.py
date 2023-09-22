def repetidos (lista):
    """Retorna o número de vezes que um elemento da lista é igual ao elemento
    anterior. list-> int"""
    i = 0
    rep = []
    while i +1 < len(lista):
        if lista[i] == lista[i+i]:
            rep = rep + [lista[i],]
        i = i+1
    return len(rep)