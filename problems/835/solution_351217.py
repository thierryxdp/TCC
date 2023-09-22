def melhor_volta(matriz):
    '''Retorna uma tupla com informações sobre a melhor volta de quem
    list(list,list,...) --> tuple'''

    melhor_volta = float('inf')
    retorno = ()
    for corredor in matriz:
        i = matriz.index(corredor)+1
        for volta in corredor:
            j = corredor.index(volta)+1
            if volta < melhor_volta:
                melhor_volta = volta
                retorno = (i,melhor_volta,j)       

    return retorno