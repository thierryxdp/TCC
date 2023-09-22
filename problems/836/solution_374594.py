def busca("x" ,matriz):
    '''docs
    x->str'''
    dados=[]
    for i in range(len(matriz)):
        funcionario=matriz[i]
        
        if setor in funcionario:
            nome=funcionario[0]
            registro=funcionario[1]
            telefone=funcionario[2]
            resultado=[nome,registro,telefone]
            dados.append(resultado)
	return dados