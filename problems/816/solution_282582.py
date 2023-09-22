def maiores(lista_numero,n):
    """Dado uma lista de números inteiros e um número n, retorna a lista
    em ordem crescente à partir dos números maiores que n:
    list,int-->list"""
        lista_numero.sort()
        lista_numero=lista_numero[lista_numero.index(n)+1:len(lista_numero)]
        return lista_numero