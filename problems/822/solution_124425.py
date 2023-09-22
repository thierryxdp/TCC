def repetidos(l):
    """Retorna o numero de vezes que um elemento da lista é igual ao elemento anterior
    list -> int"""
    count = 0
    for i in range(len(l)):
        if l[i] == l[i-1]:
            count += 1
    return count