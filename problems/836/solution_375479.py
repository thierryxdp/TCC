def busca(setor,matriz):
    '''Recebe uma matriz e o setor da empresa e retorna
    os dados de todos os funcionarios'''
    '''list,str->list'''
    dados=[]
    for i in range(len(matriz)):
        funcionario=matriz[i]
        if setor in funcionario[0]:
            nome=funcionario[0]
            registro=funcionario[1]
            telefone=funcionario[3]
            resultado=[nome,registro,telefone]
            dados.append(resultado)
    return dados