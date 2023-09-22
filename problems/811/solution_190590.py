def colchao(dimensao,H,L):
    """Funcao para decobrir se um colchao passa por uma porta, dada suas dimensoes:
    lista com as dimensoes do colchao em cm ordenadas do menor para o maior e dois inteiros (H, L) correspondentes respectivamente a altura e largura da porta.
    list, int, int -> bool"""

    A, B, C = dimensao
    if B <= H or C <= H:
        return True
    elif B > H and C > H:
        return False
    else A > L:
        return False
   
    else:
        return True