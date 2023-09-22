def melhor_volta(matriz:list) -> tuple:
    """Função que, dada uma matriz 6 x 10 com os tempos
    em segundos de cada volta que os corredorres fizeram,
    retorna de quem foi a melhor volta, com qual tempo
    e em que volta."""
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    menor_volta = 100000
    
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] < menor_volta:
                menor_volta = matriz[i][j]
                volta = j+1
                corredor = i+1
    resultado = (corredor, menor_volta, volta)
    
    return resultado