def maiores(lista,n):
    if n in lista:
        quant_n=list.count(lista,n)
        n1=list.index(lista,n)
        list.sort(lista)
        return lista[n1+quant_n:-1]