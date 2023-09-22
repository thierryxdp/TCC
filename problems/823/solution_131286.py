def faltante(lista):
    """Ao fornecer uma lista com N - 1 inteiros enumerados de 1 a N
    cuja numeração representa cada peça do jogo, retorna a peça faltante.
    
    list -> int"""
    
    list.sort(lista)
    indice = 0
    comparativo = list(range(1,max(lista)+1))

    while lista[indice] == comparativo[indice]:
        indice += 1

    return comparativo[indice]