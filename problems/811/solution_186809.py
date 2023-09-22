def colchao(medidas,H,L):
    """funcao que retorna se um colchao passa pela porta ou
    não, dados de entrada uma lista com as medidas do colchao
    em centimetro, da menor para a maior, e as dimensoes da
    porta, tambem em centimetros, altura (H) e largura (L);
    list,int,int -> bool"""

    return (medidas[0]<=L and medidas[1] <=H) or (medidas[0]<=H and medidas[1] <=L)