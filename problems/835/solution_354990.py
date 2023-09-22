def melhor_volta(matriz):
    '''funcao que retorna a melhor volta da prova, com qual foi o melhor tempo e em que
volta, dado um pista de Kart com 10 voltas para cada um dos 6 corredores
list->tupla'''
    melhores=[]
    for corredor in matriz:
            melhores =[min(corredor)]+ melhores
    melhor=min(melhores)
    melhores=melhores[::-1]
    corredor=list.index(melhores,melhor)
    volta=list.index(matriz[corredor],melhor)
    
    return (melhor, corredor+1,volta+1)