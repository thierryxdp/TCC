def repetidos(x):
    """
    Recebe uma lista de numeros e retorna o numero de vezes que um
    elemento da lista é igual ao anterior;
    list -> int
    """
    x.sort()
    i = 0
    k = []
    while i<=len(x)-1:
        if x[i]==x[0] and x.count(x[0]) == 1:
            k.append(x[i])
        i = i + 1
    return len(k)