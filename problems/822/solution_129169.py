def repetidos(lista):
    """Funcao que dada uma lista de numeros como entrada, retorna o numero de vezes
    que um elemento da lista é igual ao elemento anterior; list -> int"""

    contador = 0
    posicao = 0
    
    while posicao < len(lista):
          if lista[posicao] == lista[posicao+1]:
            contador = contador + 1
            posicao = posicao + 1
    return contador