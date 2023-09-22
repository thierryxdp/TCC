def melhor_volta(lista):
    """Dado uma matriz com os tempos dos corredores em cada volta, a função retorna uma tupla informando quem obteve a melhor volta, o tempo dessa volta e o número da volta, respectivamente;
    lista[list...]->tuple"""
    avaliacao=[]
    for i in range(len(lista)):
        list.append(avaliacao,min(lista[i]))
    tempo= min(avaliacao)
    corredor=list.index(avaliacao,tempo)+1
    volta=list.index(lista[corredor-1],tempo)+1
    return (corredor,tempo,volta)