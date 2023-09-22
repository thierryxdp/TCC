def repetidos(lista):
    """Dada uma lista de números, esta função retorna o número de vezes que algum elemento da lista é igual ao seu antecessor; list -> int"""
    vezes_repetidas = 0
    posicao = 0
    
    while posicao < len(lista) - 1 :
        if lista[posicao] ==  lista[posicao + 1]:
            vezes_repetidas = vezes_repetidas + 1
        posicao = posicao  + 1
    return vezes_repetidas