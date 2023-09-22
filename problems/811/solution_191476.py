def colchao(medidas,H,L):
    '''calcula se o colchao com certas medidas passa ou não pelas portas
    list,float,float->bool'''
    x=[H,L]
    list.sort(medidas)
    list.sort(x)
    return medidas[0] <= x[0] and medidas[1] <= x[1]