def melhor_volta(matriz):
    '''Função que dada uma matriz com os resultados de uma corrida,
    retorna uma tupla contendo o vencedor, o tempo da melhor volta e qual foi a melhor volta.
    matriz -> list
    return -> tuple'''
    
    lista_tempos = []
    for linha in range(len(matriz)):
        lista_tempos += [min(matriz[linha])]
        menor_tempo = min(lista_tempos)
        
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == menor_tempo:
                vencedor = linha + 1
                volta = coluna + 1
                
               
        
            
            
    return vencedor, menor_tempo, volta