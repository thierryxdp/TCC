def maiores(numeros, n):
#essa função seleciona o numeros maiores que 'n' da lista e os retorna ordenadamente.
#list, int -> list
    tam = list()
    for c in numeros:
        if(c>n):
            tam.append(c)
    tam.sort()
    return tam