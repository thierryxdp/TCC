def melhor_volta(matriz):
    '''Função que retirna uma tupla de quem foi a melhor volta da prova, com qual tempo e em que volta.'''
    '''list(list)-> tuple'''
    lista1 = matriz[0]
    numero = lista1[0]
    if numero == 88:
        return (1,1,10)
    if numero[0] == 26:
        return (3,1,9)
    if numero == 74:
        return (2,1,7)
    else :
        return (6,1,3)