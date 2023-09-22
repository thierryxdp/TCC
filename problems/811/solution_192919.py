def colchao(medidas,H,L):
    """Função que dada uma lista com as dimensôes A x B x C de
    um colchão em centimetros, ordenadas da menor para a maior e
    dois inteiros H e L, correspondentes a altura e largura das portas
    em centimetros, retorna se é possível passar o colchão pelas portas;
    lista, int, int -> bool"""

    listaA = list(medidas)
    listaH = listaA[1]
    listaL = listaA[0]

    if (listaH < H and listaL < L) or (listaH == H and listaL < L):
        return True 
    else:
        return False