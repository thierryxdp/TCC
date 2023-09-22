def filtraMultiplos(lista,n):
    """essa função recebe uma lista e um valor 'n' 
    e retorna uma nova lista contendo apenas os números mutiplos de 'n';
    list,int-->list"""
    l = []
    i = 0
    while i < len(lista):
        if lista[i]%n==0:
            l.insert(i,lista[i])
        i = i + 1
    return l