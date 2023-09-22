def colchao(medidas,H,L):
    'dadas as medidas de um colchao e da porta, retorna se o colchao passa ou nao por ela. list, int-> bool'
    if (medidas[0]<L and medidas[1]<H) or (medidas[0]<H and medidas[1]<L):
        return 'True'
    else:
        return 'False'