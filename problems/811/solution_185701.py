def colchao(medidas,H,L):
    """Calcula se o colchão irá passar da porta, sendo (medidas) uma lista
    com os tamanhos inteiros A,B,C do colchão e H e L, os tamanhos inteiros
    da altura e largura da porta; list,int,int->bool"""
    return (medidas[0]<L and medidas[2]<H)or(medidas[1]<H and medidas[0]<L)or(medidas[1]<H and medidas[2]<L)or
(medidas[2]<L and medidas[0]<H)