def repetidos(x):
    """
    Recebe uma lista de numeros e retorna o numero de vezes que um
    elemento da lista é igual ao anterior;
    list -> int
    """
    i = 0
    k = []
    n = 0
    while i<=len(x):
        if x[i]==n:
            k.append(x[i])
        i = i + 1
        n = n + 1
        
    return len(k)