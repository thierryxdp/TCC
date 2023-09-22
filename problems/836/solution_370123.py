def busca(setor, matriz):
    '''Função que recebe uma matriz como a do exemplo e faz uma busca por setor
    list -> list'''
    
    lista_setor = []
    funcionario = []
    
    for i in matriz:
        funcionario = i[:]
        if funcionario[2] == setor:
            del funcionario[2]
            list.append(lista_setor, funcionario)
            
    return lista_setor