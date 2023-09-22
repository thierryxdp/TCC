def melhor_volta(matriz):
    '''função que dada uma matriz comm os tempos de cada volta de cada corredor
    retorna a melhor volta, com o corredor e qual foi a volta
    entrada:list
    saida: tuple'''
    melhor= ()
    for x in matriz:
        melhor.append(min(x))
    return melhor