def melhor_volta(matriz):
    '''Função que recebe uma matriz 6 x 10, cujas linhas representam
    	os corredores de uma psita de Kart e cada coluna representa
        os seus tempos para cada uma das 10 voltas. A função retorna
        quem teve a melhor volta, qual foi o tempo pra realizá-la e 
        em que volta esse tempo foi alcançado
        
        list(list) -> tup'''
    menor = []
    volta = []
    corredor = []
    for linha in matriz:
        menor = menor + [min(linha)]
        for coluna in linha:
            if min(menor) == coluna:
                volta = list.index(linha, coluna) + 1
                corredor = list.index(matriz, linha) + 1
    return (corredor, min(menor), volta)