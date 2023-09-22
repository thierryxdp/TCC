def colchao(medidas,H,L):
    """Esta função retorna True ou False caso um colchão consiga passar ou não por uma porta de dimensões H e L, dado as dimensões do colchão em centimetros,
    ordenadas da menor para a maior e dois inteiros H e L que é a altura e a largura das portas."""
    if medidas[1]<=L and medidas[2]<=H:
        return True
    if medidas[0]<=L and medidas[1]<=H:
        return True
    if medidas[0]<=L and medidas[2]<=H:
        return True
    else:
        return False