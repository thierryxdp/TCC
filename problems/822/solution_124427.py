def repetidos(l):
    """Retorna o numero de vezes que um elemento da lista é igual ao anterior
    list > int"""
    count = 0
    i = 0
    while i < len(l):
        if l[i] == l[i-1]:
            count += 1
        i+=1
    return count