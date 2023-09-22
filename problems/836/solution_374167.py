def busca(setor, matriz):
    '''docs'''
    busca_funcionarios = []
   #linha = funcionario
   #coluna = informações do funcionario
    for linha in range(len(matriz)):
        if matriz[linha][2] == setor:
            del matriz[linha][2]
            busca_funcionarios.append(matriz[linha])
            
    return busca_funcionarios