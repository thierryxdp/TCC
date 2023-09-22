def busca(setor, matriz):
    '''docs'''
    busca_funcionarios = []
   #linha = funcionario
   #coluna = informações do funcionario
    for linha in range(len(matriz)):
        if matriz[linha][2] == setor:      
            busca_funcionarios.append(matriz[linha])
            
            busca_funcionarios[linha].remove(setor)
            
    return busca_funcionarios