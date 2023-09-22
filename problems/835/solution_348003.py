def melhor_volta(matriz):
    '''Função que retorna o melhor tempo, qual corredor e a
    melhor volta. Lista - > Tupla'''
    v = 0
    volta = 0
    a = 0
    corredor = 0
    for linha in matriz:
        C = list(range(1,len(matriz)+1)
        for i in range(len(linha)):
                 if linha[i] < linha[v]:
                 v = i
                 volta = linha[v]
                 corredor = C[a]
        a = a + 1   
            
    return (corredor,linha[v],volta)