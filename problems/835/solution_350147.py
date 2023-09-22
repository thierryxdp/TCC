def melhor_volta(matriz):
    """Dada uma matriz contendo o tempo em segundos
    de 6 corredores ao longo das 10 voltas em uma pista
    de Kart, a função retorna uma tupla contendo de quem
    foi a melhores volta, qual foi o tempo e em que volta
    isso ocorreu.
    Parametros de Entrada: list
    Retorna: tupla"""

    tempo=[]
    corredor=1
    volta=1
    
    for i in matriz:
        tempo=tempo+[min(i)]
    menor_tempo=min(tempo)
    
    corredor=corredor + list.index(tempo,menor_tempo)
    volta= volta + list.index(matriz[corredor],menor_tempo)
    
    return tuple([corredor,volta,menor_tempo])