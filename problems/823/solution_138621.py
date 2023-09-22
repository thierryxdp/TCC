def faltante(lista):
    """
    funçao que dada uma lista de numeros que caso o numero nao
    estiver dentro do intervalo [1,N] retorna o numero faltante.
    :param lista: list 
    :return: int 
    """
    contando = 0
    lista_ordenada = sorted(lista)

    while contando < len(lista):
        if contando + 1 == lista_ordenada[contando]:
            contando += 1

        else:
            return contando + 1

    return contando + 1