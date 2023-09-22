def busca(setor, matriz):
    '''busca e retorna os dados de todos os funcionarios tendo o 
    setor como parametro fornecido.
    string,list --> list'''
    
    funcionario = []
    
    for i in range(len(matriz)):
        if setor in matriz[i]:
            list.append(funcionario,matriz[i])
    for i in range(len(funcionario)):
        list.remove(funcionario,setor)
        
        
    return funcionario