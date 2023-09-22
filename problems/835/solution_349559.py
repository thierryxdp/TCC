def melhor_volta(m):
    '''
    list ----> tuple
    retorna tupla com o carro da melhor volta
    em que volta foi e quanto levou
    '''
    retorno = () 
    tempos = []
    for i in range(len(m)):
        for k in range(len(m[0])):
            tempos+=[m[i][k]]
    tempo_minimo = min(tempos)
    for i in range(len(m)):
        for k in range(len(m[0])):
         if tempo_minimo in m[i][k]:
           retorno =(i,tempo_minimo,k+1)
    return retorno