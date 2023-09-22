#---------------------EXERCICIO 4---------------------

def melhor_volta(matriz):
    '''Retorna quem teve a melhor volta, seu tempo e qual volta
        ASSUME matriz 6X10 com tempos em segundos
       list -> tuple'''

    menoresTempos = [min(matriz[0]),min(matriz[1]),min(matriz[2]),min(matriz[3]),min(matriz[4]),min(matriz[5])] #acumula menores tempos de cada corredor
    vencedor = [] #acumula dados do vencedor até o momento
    
    for contaCorredor in range(len(menoresTempos)):
        if menoresTempos[contaCorredor]==min(menoresTempos):
            vencedor.append(contaCorredor+1)
            vencedor.append(menoresTempos[contaCorredor])
    
    for contaVolta in range(len(matriz[vencedor[0]-1])):
        if matriz[vencedor[0]-1][contaVolta] == vencedor[1]:
            vencedor.append(contaVolta+1)
    
    return (vencedor[0],vencedor[1],vencedor[2])