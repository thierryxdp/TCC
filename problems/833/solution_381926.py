def conta_numero(numero,matriz):
    """ a funçao recebe um numero int e uma matriz e retorna a quantidade de vezes
    que o numero aparece na matriz;
    int,list->int"""
    l = []
    m = matriz
    n = numero
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == n:
                list.append(l,1)
            else:
                list.append(l,0)
    return lista.count(1)