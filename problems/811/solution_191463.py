def colchao(medidas,H,L):
    '''calcula se o colchao com certas medidas passa ou não pelas portas
    list,float,float->bool'''
    x=list.sort(medidas)
    return x[0]<=H and x[1]<=L