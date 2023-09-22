def faltante(lista):
    """
    funçao que dada uma lista de numeros inteiros[n-1] numerados de 1 a n, rettorna o numero fora do inervalo dado 
    :param lista: list 
    :return: int 
    """
    cont = 0
    lista_ordenada = sorted(lista)

    while cont < len(lista):
        if cont + 1 == lista_ordenada[cont]:
            cont+= 1

        else:
            return cont + 1

    return cont+ 1