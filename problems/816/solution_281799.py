def maiores(numeros_inteiros,n):
    ni = list.insert(numeros_inteiros,n,-1)
    list.sort(ni)
    return ni[n:]