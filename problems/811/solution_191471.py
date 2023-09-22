def colchao(medidas,H,L):
    '''calcula se o colchao com certas medidas passa ou não pelas portas
    list,float,float->bool'''
    x=medidas.sort
    (x[0]<=H and x[1]<=L) or (x[0]<=L and x[1]<=H)