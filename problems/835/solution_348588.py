# questão 4 - OK!
def melhor_volta(matriz):
    """ Dada um uma matriz com os tempos de 10 voltas de  6 corredores, vamos retormar qual corredor foi a melhor volta, qual o tempo e em qual volta esse tempo aconteceu.
        Parametros:
        Entrada -> matriz : list
        Saida   -> tupla   """
    
    m=matriz
    num_linha=len(m)
    num_coluna=len(m[0])
    melhores=[]
    for i in range(num_linha):
        x=min(m[i][:])
        list.append(melhores,x)
    menor=min(melhores)
    piloto=melhores.index(menor)
    y=list.index(m[piloto],menor)
    

    return piloto+1 , menor , y+1