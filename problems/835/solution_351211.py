def melhor_volta(matriz):
    '''Retorna uma tupla com informações sobre a melhor volta de quem
    list(list,list,...) --> tuple'''

    melhor_volta = float('inf')
    retorno = ()
    for corredor in matriz:
        i = matriz[matriz.index(corredor)]	
        for volta in corredor:
            j = corredor[volta]
            if volta < melhor_volta:
                melhor_volta = volta
                retorno = (i,j,melhor_volta)       

    return retorno