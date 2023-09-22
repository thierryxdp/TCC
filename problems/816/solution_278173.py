def maiores(lista_numeros,n):
    return list(.sort(filter( lambda e: e >= n ,lista_numeros)))