def colchao(medidas,H,L):
    """Função que, dadas as dimensões 'A', 'B' e 'C' de um colchão - fornecidas em ordem
crescente -, e altura e largura ('H' e 'L', respectivamente) da porta por onde o colchão deve
passar, retorna True se for possível a passagem ou False se não for possível."""
    """list, int, int-->bool"""
        
    if medidas[1]>H:
        return False
    else:
        return True