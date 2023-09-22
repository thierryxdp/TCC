def maiores(lista,n):
    " " "Retorna os numeros de uma lista maiores que um numero(n);list, int, ->list" " " 
    list.append(lista,n)
    list.sort(lista)
    a = list.index(lista,n)
    return lista[a+1:]