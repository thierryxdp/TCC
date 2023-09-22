def melhor_volta(m):
    '''recebe uma matriz 6x10 com os tempos em segundos dos corredores em cada volta e retorna de quem foi a melhor volta (entre os corredos de 1 a 6), o tempo dessa volta e em que volta esse tempo ocorreu.
    matriz -> tupla'''
    melhortempo = m[0][0]
    for i in range(6):
        if min(m[i]) <= melhortempo:
            melhortempo = min(m[i])
            corredor = i + 1
            volta = list.index(m[i],melhortempo) + 1
    return (corredor,melhortempo,volta)