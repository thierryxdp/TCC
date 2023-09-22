def colchao(medidas,H,L):
"""Retorna se e possivel passar o colchao pela porta dado as medidas do colchao como o primeiro parametro, a altura da porta como o segundo e a largura da porta como o ultimo parametro;
list,int,int->bool"""
if medidas[0]<H and medidas[1]<L or medidas[0]<L and medidas[1]<H or medidas[0]<H and medidas[2]<L or medidas[0]<L and medidas[2]<H or medidas[1]<L and medidas[2]<H or medidas[1]<H and medidas[2]<L:
    return 'True'
else:
    return 'False'