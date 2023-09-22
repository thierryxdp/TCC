def melhor_volta(matriz):
    '''Função identifica e retorna através de uma tupla: melhor corredor,
    tempo do melhor corredor e em qual volta pertence esse melhor tempo;
    matriz -> tupla'''
    menores = [] #Lista de menores tempos
    volta = [] #Lista de voltas

    for linhas in matriz:
        menores.append(min(linhas))
        volta.append(linhas.index(min(linhas)) + 1)
    corredor = menores.index(min(menores)) + 1 #Através da função INDEX descobre o corredor graças a lista de menores tempos da corrida. O +1 foi add por o indice começar no 0
    volta = volta[menores.index(min(menores))] #Segue a mesma lógica acima. 

    return (corredor,min(menores),volta)