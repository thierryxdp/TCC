def melhor_volta(m):
    '''recebe uma matriz 6x10 com os tempos em segundos dos corredores em cada volta e retorna de quem foi a melhor volta (entre os corredos de 1 a 6), o tempo dessa volta e em que volta esse tempo ocorreu.
    matriz -> tupla'''
    melhortempo = m[0][0]
    for j in range(len(m)):
        if min(min(m)) <= melhortempo:
            melhortempo = min(min(m))
    		corredor = list.index(m,min(m)) + 1
    		volta = list.index(m[corredor-1],min(min(m))) + 1
    return (corredor,melhortempo,volta)