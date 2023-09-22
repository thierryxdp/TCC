def colchao(medidas, H,L):
    """Função que dado as medidas do colchão em cm(medidas), a altura da porta da casa(H) e
    a largura da porta(L) retorna se o colchão passa pelas portas da casa ou não.
    lista, int, int -> bool"""

    if ((medidas[0] <= L) and (medidas[1] < H)):
        return True
    elif ((medidas[0] <= H) and (medidas[1] < L)):
        return True
    else:
        return False