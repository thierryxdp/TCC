def colchao(medidas,H,L):
"""Retorna se o colchão passa ou não pela porta"""
if medidas[0]<H and medidas[1]<L or medidas[0]<L and medidas[1]<H or medidas[0]<H and medidas[2]<L or medidas[0]<L and medidas[2]<H or medidas[1]<L and medidas[2]<H or medidas[1]<H and medidas[2]<L:
    return 'True'
else:
    return 'False'