def busca(setor,matriz):
    '''Recebe uma matriz e faz uma busca por setor, retornando os dados
    de todos os funcionários daquele setor
    str,mat->list'''
    retorno=[]
    for funcionario in matriz:
        if setor in funcionario:
            funcionario=list.remove(funcionario,setor)
            retorno=retorno+[funcionario]
    return retorno