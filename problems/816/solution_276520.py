def maiores (lista_numeros,n):
    if list.count(lista_numeros,n) == 0 and (sorted(lista_numeros)[len(lista_numeros) - 1])>n:
        return sorted(lista_numeros)[0:list.index(sorted(lista_numeros) + [n],n)]
    
    if list.count(lista_numeros,n) == 0 and (sorted(lista_numeros)[len(lista_numeros) - 1])<n:
        return []