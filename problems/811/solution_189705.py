def colchao(medidas,H,L):
    """Função retorna se é possível passar um colchão por uma porta dadas
sua altura e largura e as medidas do colchão;
list, int, int -> bool"""
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]

    if (A <= L or A <= H) and (B <= L or B <= H):
        return True
    else:
        return False