def melhor_volta(matriz):
    """Função que dada uma matriz com os tempos das 10 voltas dos 6
    corredores de kart, retorna uma tupla com quem fez o melhor
    tempo, qual foi esse tempo e em qual volta;
    list -> tuple"""
    tempo=0
    melhor_corredor=0
    melhor_volta=0
    corredor=0
    for linha in matriz:
        corredor+=1
        volta=0
        for e in linha:
            volta+=1
            if tempo == 0 or e<tempo:
                tempo=e
                melhor_corredor=corredor
                melhor_volta=volta
    return melhor_corredor,tempo,melhor_volta