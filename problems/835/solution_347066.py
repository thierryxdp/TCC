def melhor_volta(tempos):
    """Funcao que informa a melhor volta (com tempo e volta);
    entrada: list
    saida: tuple"""
    corredor=0
    tempo=[]
    volta=0
    contador=0
    while contador < len(tempos):
        for i in range(len(tempos[contador])):
            list.append(tempo,tempos[contador][i])
        contador+=1
    contador=0
    tempo = min(tempo)
    while contador < len(tempos):
        if tempo in tempos[contador]:
            corredor = contador
            volta = list.index(tempos[contador],tempo)
        contador+=1
    corredor+=1
    volta+=1   
    return corredor,tempo,volta