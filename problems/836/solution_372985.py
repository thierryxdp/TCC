def busca(setor,matriz):
    '''Função que, dada uma matriz com informações de funcionários e uma string de um setor específico, retorna os dados de todos os funcionários daquele setor; list[list], str -> list'''
    resultado=[]
    for info_funcionarios in matriz:
        if info_funcionarios[2]==setor:
            list.remove(info_funcionarios,setor)
            list.append(resultado,info_funcionarios)
    return resultado