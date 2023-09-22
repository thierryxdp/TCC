def maiores(numeros_inteiros,n):
    ni = numeros_inteiros + [n]
    list.sort(ni)
    return ni[n:]