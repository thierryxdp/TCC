def filtraMultiplos(m, n):
    '''Retorna a lista de números divisiveis por um número, a partir desse número e de uma lista de possíveis divisores desse
    list(float), float -> list(float)'''
    l = []
    x=0
    while x<=len(m):
        if m[x]%n==0:
            list.append(l, m[x])
        x+=1
    return l