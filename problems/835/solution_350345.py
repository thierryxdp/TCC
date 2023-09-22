def melhor_volta(matriz):
    '''Recebe uma matriz 6x10 informando o tempo de cada volta de cada corredor
    (número da linha = número do corredor; número da coluna = número da volta) e 
    retorna uma tupla de qual corredor foi a menor volta, o tempo e o número da volta;
    list(list) -> tuple(int,float,int)'''
    lista = []
    for i in range(len(matriz)):
        for j in matriz[i]:
            lista += [j]
    menor_tempo = min(lista)
    for i in range(len(matriz)):
        for j in matriz[i]:
            if j == menor_tempo:
                numero_corredor = i + 1
                numero_volta = j + 1
    return (numero_corredor,menor_tempo,numero_volta)