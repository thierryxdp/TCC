def melhor_volta (matriz):
    '''função que dada a uma matriz com os tempos de cada corredor
    de kart, retorna quem teve a melhor volta, com qual tempo
    e em que volta, respectivamente.
    list -> tuple'''
    
    corredor = []
    
    
    for i in range(len(matriz)):
        corredor += [sum (matriz[i])]
    melhor_tempo = min (matriz [list.index(corredor,min(corredor))])
    volta = list.index (matriz [list.index (corredor,min(corredor))],melhor_tempo)
    
    return (list.index(corredor,min(corredor)),melhor_tempo,volta)