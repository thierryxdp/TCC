def colchao(lista,H,L):
    """Dada uma lista com as dimensões de um colchão em ordem crescente, a altura e largura de uma porta, respectivamente, essa função nos diz se de alguma forma, o colchão consegue passar pela porta; list, int, int -> booleano"""
    if (lista[0] <= H and lista[1] <= L) or (lista[1] <= H and lista[0] <= L):
        return True
    else:
        return False