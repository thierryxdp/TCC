def maiores(lista,n):
    """Funçao que dada uma lista de um numero int e um numero n int, retorna outra lista com todos os numeros maiores que n de forma crescente int,int=>int"""
    maiores= list()
    lista.sort()
    for c in lista:
        if c >= n:
            maiores.append(c)
            return maiores