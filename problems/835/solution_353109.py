def melhor_volta(m):
    '''
    	Função que receba como entrada uma matriz 6 x 10 com os tempos
        em segundos dos corredores em cada volta.Deve retornar uma tupla 
        informando: De quem foi a melhor volta da prova,
        com qual tempo e em que volta.
        m:int
        contador:int
        acumulador:int
        min:int
        return:tupla
    '''
    contador = 0
    acumulador = 0
    min = 999999
    i = 0
    j = 0
    if len(m) != 0:
        while i < len(m):
            j = 0
            while j < len(m[i]):
                if m[i][j] < min:
                    min = m[i][j]
                    mc = i
                    mv = j
                j += 1
            i += 1
        return (mc+1, min, mv+1)