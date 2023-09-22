def maiores(numeros, n):
#essa função recebe uma lista de numeros e retorna uma outra lista com somente os numeros maiores que 'n'
    tam = []
    for c in numeros:
        if(c>n):
            tam.append(c)
    tam.sort()
    return tam