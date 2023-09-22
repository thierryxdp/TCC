def melhor_volta(m):
    '''Funcao que recebe como entrada uma matriz 6x10 com os tempos
    dos corredores e retornauma tupla informando de qeuem foi a melhor
    volta da prova,com qual tempo e em qual volta. list-> tuple '''
    
    ord1=[]
    for i in range(1,7):
        menores= ord1[0]
        for j in range (1,11):
            ord1+=[m[i][j]]
            ord1 = min(ord1)
    return menores