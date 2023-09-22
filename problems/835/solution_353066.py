def melhor_volta(matriz):
    '''funçao  que verifica quem fez  a  melhor
    volta, com que tempo e em que volta'''
    'list--> tuple'

    tempos =[]
    voltas =[]
    for volta in range(6):
        for tempo in range(10):
            tempos=tempo + 1
            voltas=volta + 1
            tupla  =  (volta  +  1,  tempo,  piloto)
            return tupla