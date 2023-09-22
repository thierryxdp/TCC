def busca(setor, matriz):
    '''Função que dado uma matriz contendo informações de funcionarios e um setor de
    uma determinada empresa, retorna todos os funcionarios que fazem parte desse setor.
    setor -> string
    matriz -> list
    return -> list'''
    c = 0
    busca_funcionarios = []
   #linha = funcionario
   #coluna = informações do funcionario
    for linha in range(len(matriz)):
        if matriz[linha][2] == setor:      
            busca_funcionarios.append(matriz[linha])
            
            busca_funcionarios[c].remove(setor)
            c += 1
            
    return busca_funcionarios