def busca(setor,matriz):
    '''
        Função que recebe uma string (setor) e uma matriz com
        as colunas caracterizando nome, registro, setor e telefone,
        nessa ordem, de um funcionário, e as linhas representando
        a quantidade de funcionarios (matriz) e retorna uma busca
        por setor, ou seja, dado o nome de um setor da empresa, a
        função retorna uma lista com os dados de todos os funcionários
        daquele setor. Se nenhum registro for encontrado, a função
        irá retornar uma lista vazia;
        str,list->list
    '''
    funcionarios=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            funcionarios+=[matriz[i]]
    for i in range(len(funcionarios)):
        funcionarios[i].remove(setor)
    return funcionarios