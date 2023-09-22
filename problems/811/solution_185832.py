def colchao(medidas,H,L):
    """funcao que recebe como entrada um lista das medidas de 
    um colchao, em ordem crescente de valores, e determina se 
    um certo colchao passa pela porta(dadas a altura e largura
    da porta). Retorna True se o colchao passar e false se nao 
    passar.
    list,int,int->bool"""
    [A,B,C]=medidas
    
    if B<=H or B<=L:
        return True
    else: return False