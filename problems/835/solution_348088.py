def melhor_volta(matriz):
    '''Função que recebe um matriz com os tempos em segundos
    dos corredores em cada volta e retorna uma tupla informando de quem 
    foi a melhor volta, com qual tempo e em que volta.
    lista -> tupla'''
    
    tempo_final=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            menor_tempo=min(matriz[i])

        tempo_final.append(menor_tempo)
        resultado=min(tempo_final)
        if matriz[i][j]==resultado:
            posicao=j
        
    return volta, resultado, posicao