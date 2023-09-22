def busca(setor,matriz):
    '''dada uma matriz com informacoes de funcionarios e um setor, retorna as informacoes dos funcionarios que estao no determinado setor; str,list -> list'''
    lista = []
    for funcionario in matriz:
        if funcionario[2] == setor:
            lista += funcionario
    return lista