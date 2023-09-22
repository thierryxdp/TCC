def melhor_volta(matriz):
    '''dada uma matriz 6x10 informando o tempo de cada corredor, calcula e retorna quem deu a melhor volta, o tempo e em que volta
list-> tuple'''
    J = []
    for i in matriz:
        list.append(J, min(i))
        a = list.index(J, min(J))
    b = list.index(matriz[a], min(J))    
    y = (a + 1, min(J), b + 1)    
    return y