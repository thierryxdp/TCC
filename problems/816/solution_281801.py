def maiores(numeros_inteiros,n):
    list.insert(numeros_inteiros,-1,n)
    ni = numeros_inteiros
    list.sort(ni)
    return ni[n:]