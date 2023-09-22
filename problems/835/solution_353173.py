def melhor_volta(matriz):
    '''é essa!!!!!!!!!!!!!!!!!!!!!'''
    
    lista_tempos = []
    for linha in range(len(matriz)):
        lista_tempos += [min(matriz[linha])]
        menor_tempo = min(lista_tempos)
        
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] == menor_tempo:
                vencedor = linha + 1
                
    volta = matriz[vencedor].index(menor_tempo)
        
            
            
    return vencedor, menor_tempo, volta