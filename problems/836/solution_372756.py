def busca(setor, funcionarios):
    """ Recebe uma matriz e faz uma busca por setor, ou seja, dado um nome de 
    um setor da empresa, a função retorna os dados de todos os funcionários daquele setor
    list -> list """
    saida = []
    for funcionario in funcionarios:
        if funcionario[2]==setor:
            encontrado = funcionario[:]
            del encontrado[2]
            list.append(saida, encontrado) 
    return saida