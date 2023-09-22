# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """dados as dimensões do colchão por uma lista em medidas, a altura H e a largura L da porta,
    a função retorna um valor booleano se o colchão passa pela porta;
    os dados estão em centímetros;
    list(float,float,float),float,foat->bool"""
    H_colchao=medidas[2]
    L_colchao=medidas[1]
    E_colchao=medidas[0]
    if H_colchao>H and L_colchao>H:
        return False
    if L_colchao>L and L_colchao>H:
        return False
    elif L_colchao>H and H_colchao<L:
         return True
    else:
        return True