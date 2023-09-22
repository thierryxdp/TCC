def maiores(numeros_inteiros,n):
    ni = list.insert(numeros_inteiros,-1,n)
    list.sort(ni)
    return ni[n:]