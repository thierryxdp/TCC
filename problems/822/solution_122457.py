def repetidos(lista):
    """Dada uma lista numérica retorna o número de vezes que um dado elemento da lista
       é numéricamente igual do que o seu sequêncial.
       list -> list"""
    
    posicao = 0
    
    while posicao < len(lista):
        if lista[posicao] / lista[posicao+1] == 1:
            prosicao = posicao + 1
            return posicao