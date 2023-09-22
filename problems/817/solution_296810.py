def maiores(lista,n):
    """Funcao que retorna os numeros de uma lista maiores que n 
    ordenados de forma crescente
    entrada: list, int
    saida: list"""
    x = lista + [n]
    list.sort(x)
    z = list.index(x,n)
    del x[:z+1]
    return x
def acima_da_media(notas):
    """Funcao que retorna a lista de notas ordenada com as notas
    que ficaram acima da media
    entrada:list
    saida: list"""
    return maiores(notas,6)