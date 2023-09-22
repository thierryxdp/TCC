def busca(setor, matriz):
    '''Função que recebe uma matriz como a do exemplo e faz uma busca por setor
    list -> list'''
    
    setor = []
    funcionario = []
    
    for i in matriz:
        funcionario = i[:]
        if funcionario[2] == setor:
            list.append(setor, funcionario)
            
    return setor