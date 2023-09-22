def faltante(lista:list) -> int:
    i = 0
    lista.sort()
    while i < len(lista):
        if lista[i]-1 not in lista and lista[i]-1 !=0:
                continue
            return lista[i]-1
        i+=1
    lista[-1]+1