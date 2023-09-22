def busca(setor,matriz):
    ''' docs
    '''
    dados=[]
    
    for i in range(len(matriz)):
        # busca o funcionario na linha I da matriz
        funcionario = matriz[i]
        
        if setor in funcionario:
            # extrai as informacoes do funcionario
            nome = funcionario[0]
            registro = funcionario[1]
            telefone = funcionario[3]
            
            # adiciona na lista de funcionarios
            resultado = [nome, registro, telefone]
            dados.append(resultado)
    
    return dados