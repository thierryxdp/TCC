def faltante(listaFaltante):
    """ Dada uma lista de números com um número faltante,
    essa lista faltante é ordenada corretamente e
    é feito uma lista correta com todos os números por meio do range(1, n+1),
    é feito iterações na lista faltante verificando se o número da lista dos faltantes em questão é
    diferente do número da lista correta, e se for, é retornado o número da lista correta que falta na lista faltante.
    Após essas iterações, é retornado o último número da lista faltante + 1.
    list -> int
    """
    listaFaltante.sort()
    n = max(listaFaltante)
    listaCorreta = list(range(1, n+1))
    i = 0
    while i < len(listaFaltante):
        if(listaFaltante[i] != listaCorreta[i]):
            return listaCorreta[i]
        i += 1
    return listaFaltante.pop() + 1