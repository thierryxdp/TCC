def faltante(lista):
    """Recebe uma lista de números de tamanho N-1, sendo os
    valores 1 até N, retorna o valor que falta na lista 
    original.
    list -> int"""
    list.sort (lista)
    indice = 0
    while indice < len(lista):
        if lista[indice] != lista[indice+1]:
            return int(lista[indice]) +1
        indice +=1