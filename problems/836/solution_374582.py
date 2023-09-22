def busca(matriz)):
    '''docs'''
    dados=[]
    for i in range(len(matriz)):
        funcionario=matriz[i]
        
        if setor in funcionario:
            nome=funcionario[0]
            registro=[1]
            telefone=[2]
            resultado=[nome,registro,telefone]
            dados.append(resultado)
    return dados