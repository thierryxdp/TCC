def filtraMultiplos(m, n):
    '''Retorna a lista de números divisiveis por um número, a partir desse número e de uma lista de possíveis divisores desse
    list(float), float -> list(float)'''
    l = []
    for i in range m:
        if m[i]%n==0:
            list.append(l, m[i])
    return l