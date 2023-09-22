def maiores(lista_numeros,n):
    return list(sorted(filter( lambda e: e >= n ,lista_numeros)))