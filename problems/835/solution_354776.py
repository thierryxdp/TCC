def melhor_volta(matriz):
    ''' Dada uma matriz 6x10 com os tempos em segundos dos corredores em cada
volta. Retorna uma tupla informando de que. foi a melhor volta da prova, com qual tempo e em que volta.
list(list) -> tuple''' 
    M=[]
    for linha in matriz:
        M.append(min(linha))
    quem= list.index(M,min(M))
    volta= list.index(matriz[quem],min(matriz[quem]))
    tempo= matriz[quem][volta]
    return (quem,tempo, volta)