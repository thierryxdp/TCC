def busca(setor,matriz):
    '''Retorna os dados referentes à todos os funcionários do setor dado;
    str, list -> list'''
    retorno=[]
    for funcionario in matriz:
        if funcionario[2]==setor:
            list.remove(funcionario,setor)
            list.append(retorno,funcionario)
    return retorno