def colchao(medidas,H,L):
    '''calcula se o colchao com certas medidas passa ou não pelas portas
    list,float,float->bool'''
    colchao=list.sort([medidas])
    porta=list.sort([H,L])
    colchao[0] <= porta[0] and colchao[1] <= porta[1]