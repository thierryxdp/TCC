def faltante(l):
    '''Retorna o número faltante da lista.
    list -> int''''
    list.sort(l)
    i = 0
    while i < len(l):
        if i + 1 <= len(l):
            if l[i + 1] - l[i] > 1:
                return l[i] + 1
        i += 1
    return 0