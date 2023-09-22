def colchao(medidas,H,L):
    """funcao que retorna True se um colchao pode passar pela porta da casa e False se nao,
    dados uma lista com as medidas do colchao em ordem crescente (medidas) e a altura e
    a largura das portas (H) e (L). list,int,int->bool"""
    h=medidas[1]
    l=medidas[2]
    if h<=H or l<=H and h<=L or l<=L:
        return True
    else:
        return False