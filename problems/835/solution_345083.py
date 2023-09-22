def melhor_volta(matriz):
    '''função que verifica, calcula e retorna de quem foi a melhor volta em uma corrida, informando também o tempo e a devida volta. como entrada, recebe uma matriz 6x10 com os tempos dos jogadores; list(lists) -> tuple'''
    
    quem = min(matriz)
    tempo = min(quem)
    qual = min(matriz).index(tempo)
    
    return (quem, tempo, qual)