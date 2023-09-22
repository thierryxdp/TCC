def busca(setor:str,matriz:list)->list:

    """ Função que recebe uma matriz com quatro entradas representando as
        informaçõess referentes a nome, registro, setor e telefone de um
        funcionário, nesta ordem e uma string referente ao setor. A função
        deve retornar todos os dados dos funcionários daquele setor.

    """

    n_funcionarios  = len(matriz)
    nova_lista = []

    for i in range(n_funcionarios):

        if setor == matriz[i][2]:

            list.append(nova_lista,matriz[i])

    return nova_lista