def busca(string,matriz):
    '''função que recebe uma string indicando o setor onde uma pessoa trabalha e uma matriz com os dados de vários funcionários,
retorna as informações de todas as pessoas que trabalham no setor indicado pela string.
(str,list(list)) -> list'''
    lista = []
    posicao = 0
    while posicao < len(matriz):
        if string in matriz[posicao]:
            list.remove(matriz[posicao],string)
            list.append(lista,matriz[posicao])
        posicao = posicao + 1   
    return lista