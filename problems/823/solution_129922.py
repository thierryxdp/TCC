def faltante(lista):
    """A função faltante analisa uma lista de tal forma que determina qual número nesta
    sequencia esta faltando; o método utilizado é a diferenca entre a soma da lista com todos
    os numeros - por meio da funcao range - com a soma da lista informada. Caso dê um numero
    diferente de zero, o numero faltante esta inserido no intervalo entre 1 e N; senao, é o
    próprio N."""
    posicao = 0
    faltante = 0
    while posicao<len(lista):
          if sum(list(range(lista[len(lista) - 1] + 1))) - sum(lista) != 0:
             faltante = sum(list(range(lista[len(lista) - 1] + 1))) - sum(lista)
          posicao = posicao + 1
          if sum(list(range(lista[len(lista) - 1] + 1))) - sum(lista) == 0:
            faltante = len(lista) + 1
    return faltante