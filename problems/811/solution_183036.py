def colchao(medidas,H,L):
    """Função que calcula a medidas do colchão e da porta dado os valore de entrada e retorna se é possível passar com True ou False pela porta
list,int -> str"""
    if medidas[1] > H and medidas[2] > L:
        return False
    else:
        return True