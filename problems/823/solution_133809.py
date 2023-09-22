def faltante(Lista):
    """Função que dada uma lista com números de 1 a N, descubra qual o número que falta e retorne esse número
    list -> int"""
    antecessor = Lista[-1] - 1
    sucessor = 1
    while antecessor != -1:
        if sucessor in Lista:
            sucessor += 1
        else:
            return sucessor