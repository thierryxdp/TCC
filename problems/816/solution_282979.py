def maiores(lista1,n):
    """""retorna uma lista de inteiros em ordem crescrente dos numeros maiores que n
    list, int->list"""
    numeros = [lista for lista in lista if lista > n]
    return numeros