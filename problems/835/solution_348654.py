def melhor_volta(matriz):
    '''Diz quem foi o melhor corredor;
    list(list) -> tuple'''
    pilotos = []
    # Cria uma lista com os melhores tempos
    for tempo in matriz:
        pilotos.append(min(tempo))
    melhor_tempo = min(pilotos)
    #Diz quem é o piloto com o melhor tempo
    piloto = 1
    for i in pilotos:
        if i == melhor_tempo:
           break 

        piloto = piloto + 1
    #Diz qual a melhor volta
    volta = 0
    for n in matriz[piloto - 1]
        if n == melhor_tempo:
           break
        volta = volta + 1