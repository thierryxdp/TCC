def colchao(medidas,H,L):
    """porta:H*L e colchão:medidas=[A,B,C].Define se o colchão passa pelo porta ou não"""
    
    if medidas[0]<=L and medidas[1]<=H:
        return True
    if medidas[0]<=L and medidas[2]<=H:
        return True
    if medidas[1]<=L and medidas[2]<=H:
        return True
    if medidas[1]<=L and medidas[0]<=H:
        return True
    else:
        return False
       
    # Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis