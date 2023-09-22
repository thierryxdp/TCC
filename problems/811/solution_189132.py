def colchao(medidas,H,L):
    """Recebe as medidas de um colchão, da maior para a menor, e a altura H e largura L de uma porta e verifica se o colchão passa pela porta. Todas as medidas estão em cm; int[],int,int-> bool."""
    A=medidas[0]
    B=medidas[1]
    c=medidas[2]
    if A<=H and B<=L:
        return True
    elif A<=L and B<=H:
        return True
    else:
        return False