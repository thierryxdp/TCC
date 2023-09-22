def busca(setor, matriz):
    '''docs'''
    c = 0
    busca_funcionarios = []
   #linha = funcionario
   #coluna = informações do funcionario
    for linha in range(len(matriz)):
        if matriz[linha][2] == setor:      
            busca_funcionarios.append(matriz[linha])
            c += 1
            busca_funcionarios[c].remove(setor)
            
    return busca_funcionarios