def filtraMultiplos([l],n):
    ''' retorna uma lista contendo todos os elementos da lista original que forem divisíveis por n;
    list, int -> list '''
    l1 = []
    i = 0
    while i<len(l):
        if l[i]%n == 0:
            l1 += [l[i],]
        i = i+1
    return l1