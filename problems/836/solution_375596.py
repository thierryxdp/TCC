def busca(setor, matriz):
    '''funcao que dado um setor retorna os dados de todos os funcionarios do setor'''
    funcionarios_do_setor=[]
    for funcionario in matriz:
        if setor in funcionario:
            funcionario.remove(setor)
            funcionarios_do_setor.append(funcionario)
    return funcionarios_do_setor