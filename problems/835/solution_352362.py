def melhor_volta(matriz):
    """ Essa função receberá como entrada uma matriz 6 X 10,
    sendo que cada elemento dessa matriz representará o tem-
    po em segundo efetuado por corredos em cada volta de uma
    prova. Posto isso, essa função retornará uma tupla infor-
    mando: de quem foi a melhor volta, com qual tempo e em 
    que volta.
    
    Obs: Será assumido que os corredos efetuaram tempos dife-
    rentes.
    
    list - tuple
    """
    tempos =  matriz[0] + matriz[1] + matriz[2] + matriz[3] + matriz[4] + matriz[5] + matriz[6] + matriz[7] + matriz[7] + matriz[8] + matriz[9]
    melhor_tempo = min[tempos]
    
    ret = ()
    
    for i in range(len(matriz)):
        for j in matriz[i] :
            if melhor_tempo in matriz[i]:
                ret = ret + (i,)
                ret = ret + (j,)
    return ret