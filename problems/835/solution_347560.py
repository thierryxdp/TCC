def melhor_volta(matriz):
    '''retorna o corredor que fez a melhor 
    volta, o tempo dessa volta e seu numero; list -> tuple'''
    menoresTempos=[]
    j=0
    i=0
    while j<len(matriz):
        while i<len(matriz[j]):
            menoresTempos=menoresTempos+[min(matriz[j])]
            i=i+1
        j=j+1
        i=0
    return i+1,min(menoresTempos),j+1