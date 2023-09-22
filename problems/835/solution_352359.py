def melhor_volta(matriz:list)->tuple:
    """ informa de quem foi a melhor volta da prova,com qual tempo e em que volta"""
    melho_volta=0
    tempo=20000000
    corrredor=0
    indice=1
    for i in matriz:
        if min(i)<tempo:
            tempo=min(i)
            corredor=indice
            melhor_volta=i.index(tempo)+1
        indice+=1
    return (corredor,tempo,melho_volta)