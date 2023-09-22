def conta_numero(numero, matriz):
    '''recebe um numero e listas e retorna a quantidade 
    de vezes que esse numero se repete nas listas.
    entrada: int, list
    saida: int'''
    lista = 0
    rep = 0
    while lista < len(matriz):
        rep = rep + list.count(matriz[lista],numero)
        lista = lista + 1
    return rep