def melhor_volta(matriz):
    menores_tempos = []
    voltas_mais_rapidas = []
    
    for m in matriz:
        tempo_minimo = min(m)
        menores_tempos.append(tempo_minimo)
        volta = m.index(tempo_minimo)
        voltas_mais_rapidas.append(volta)    
    
    menor_tempo = min(menores_tempos)
    posicao = menores_tempos.index(menor_tempo) 
    
    return posicao + 1, menor_tempo, voltas_mais_rapidas[posicao] + 1