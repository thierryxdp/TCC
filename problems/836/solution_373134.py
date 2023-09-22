def busca(setor,matriz):
    '''
        Dado um setor de trabalho e uma matriz contendo as informações dos funcionários
        retorna uma lista com as informações dos funcionários daquele setor.
        str,list -> list
    '''
    funcionarios=[]
    for i in matriz:
            if setor in i:
                i.remove(setor)
                funcionarios.append(i)
    return funcionarios