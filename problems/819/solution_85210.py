def filtraMultiplos(lista,n):
    """Função que recebe como entrada uma lista de números
    e um número e retorna outra lista.
    lista, int -> lista"""
    r = []
    for i in range(len(lista)):
        if lista[i] % n == 0:
            r.append(lista[i])
    return r