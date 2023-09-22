def melhor_volta(tempos):
    """Funcao que informa a melhor volta (com tempo e volta);
    entrada: list
    saida: tuple"""
    
    corredor=0
    tempo=[]
    volta=0
    
    for linha in tempos:
        tempo+=[min(linha)]
    tempo=min(tempo)
    
    for linha in tempos:
        for aij in linha:
            if linha[aij] == tempo:
                corredor=aij
            	volta = list.index(tempos[aij],tempo)
    corredor+=1
    volta+=1
    return corredor, tempo, volta