def busca(setor, matriz):
    '''Função que recebe uma matriz como a do exemplo e faz uma busca por setor
    list -> list'''
    
    setor = []
    
    for i in matriz:
        if i[2] == setor:
            list.append(setor, i)
            
    return setor