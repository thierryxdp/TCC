def busca(setor,matriz):
    '''função que recebe uma matriz com os dados dos funcionarios de uma empresa e um setor, a função busca dentro da matriz os dados do funcionario daquele respectivo setor.
    str, list(list) -> lista'''
    lista=[]
    for dado in range(len(matriz)):
        if setor == matriz[dado][2]:
            list.remove(matriz[dado],setor)
            lista = lista + [matriz[dado]]
    return listsa