def melhor_volta(matriz):
    '''Função que retorna o melhor tempo, qual corredor e a melhor
       volta. Lista - > tuple'''
    v = 0
    volta = 0
    for linha in matriz:
        volta = volta + 1
        for i in range(len(linha)):
            if linha[i] < linha[v]:
                v = i
            
    return (linha[v],v,volta)