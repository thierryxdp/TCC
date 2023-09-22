def melhor_volta(tempos):
    '''Função que, dado os valores das voltas dos pilotos, retorna dados sobre a melhor volta.
    list --> tupple'''
    menores = []
    volta = []
    for x in tempos:
        menores = menores + [min(x)]
        volta = volta + [list.index(x,min(x))]
    return (((list.index(menores,min(menores)))+1),min(menores),(volta[list.index(menores,min(menores))]+1))