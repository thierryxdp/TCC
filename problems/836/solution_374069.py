def busca(setor,matriz):
    ''' docs
    '''
    dados=[]
    
    for i in range(len(matriz)):
        if setor in matriz[i]:
            # extrai as informacoes do funcionario
            nome = matriz[i][0]
            registro = matriz[i][1]
            telefone = matriz[i][3]
            
            # adiciona na lista de funcionarios
            resultado = [nome, registro, telefone]
            dados.append(resultado)
    
    return dados