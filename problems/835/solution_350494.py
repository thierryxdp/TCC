def melhor_volta(matriz):
    "Função que dada uma matriz com os tempos de cada volta de cada atleta em uma corrida de kart, retorna a tupla contendo o corredor com a melhor volta, o tempo da volta e a volta. list --> int,float,int"
    melhortemp=min(min(matriz))
    piloto=list.index(matriz,min(matriz))
    volta=list.index(matriz[piloto],melhortemp)
    return (piloto+1,melhortemp,volta+1)