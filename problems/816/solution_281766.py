def maiores(lista,n):
    if n in lista:
        list.sort(lista)
        quant_n=list.count(lista,n)
        n1=list.index(lista,n)
        return lista[n1+quant_n:-1]