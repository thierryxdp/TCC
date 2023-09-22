def colchao(medidas,H,L):
    """Retorna True se o colchão passa pela porta e False se não, dada uma lista como parâmetro de entrada, que possui com as dimensões do colchão em centímetros, ordernadas da menor para maior, e dois inteiro H e L"""
    return (medidas[0]<=L and medidas[1]<=H) or (medidas[0]<=H and medidas[1]<=L)