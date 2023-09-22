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
    tempos =  matriz[0] + matriz[1] + matriz[2] + matriz[3] + matriz[4] + matriz[5] 
    melhor_tempo = min(tempos)
    
    ret = ()
    
    for i in range(len(matriz)):
        for j in matriz[i]:
            n = 0
            if melhor_tempo == j:
                n = n + 1
                corredor = i
                volta = n
                ret = (i+1,melhor_tempo,n)
    return ret