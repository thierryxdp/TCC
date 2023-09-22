def busca(s,matriz):
    '''Esta função recebe o nome de um setor s e uma matriz com os dados de funcionários; e
retorna uma lista com os dados dos funcionários do setor s sem a informação s.
str, list(list) --> list(str)
'''
    dados = []
    for inf in matriz:
        a = []
        if s in inf:
            list.remove(inf,s)
            print(s)
            list.append(dados,inf)
    return dados