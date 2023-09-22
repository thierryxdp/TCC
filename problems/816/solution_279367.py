def maiores(lista,n):
    '''retorna todos os numeros da lista maiores
    que n; list, int -> int'''
    list.sort(lista)
    if n in lista:
        return lista[n+1:]