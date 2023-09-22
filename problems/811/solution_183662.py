def colchao(medidas,H,L):
    """dadas as medidas do colchão, a altura H e a largura L das portas, retorna True se o colchão passa pela porta e False se não passa
    list,int,int->bool"""
    if medidas[0]<=H and medidas[1]<=L or medidas[0]<=L and medidas[1]<=H or medidas[0]<=H and medidas[2]<=L or medidas[0]<=L and medidas[2]<=H or medidas[1]<=H and medidas[2]<=L or medidas[1]<=L and medidas[2]<=H:
        return True
    else:
        return False# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis