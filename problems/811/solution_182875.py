def colchao(medidas,H,L):
    """Funcao que calcula a passagem de um colchao por uma porta, dado os valores de altura e 3 dimensoes do colchao pra ser comprado;list -> bool"""
    if medidas[1]<=H or medidas[1]<=L:
        return True 
    else: 
        return False