def melhor_volta(matriz):
    '''
    função que dada uma matrix 6x10, retorna, nessa ordem, qual linha se encontra o menor elemento
    qual o menor elemento e em qual coluna, tudo isso dentro de uma tupla
    função feita dentro do cenário de uma corrida de Kart com 6 corredores e 10 corridas, retornando,
    portanto, qual corredor teve o menor tempo, o tempo em segundos e em qual corrida
    list(list)-->tuple
    '''
    resposta= ()
    lista=matriz[0]+matriz[1]+matriz[2]+matriz[3]+matriz[4]+matriz[5]
    for i in range(6):
        for j in range(10):
            if matriz[i][j] == min(lista):
                resposta = (i+1,matriz[i][j],j+1)
    return resposta