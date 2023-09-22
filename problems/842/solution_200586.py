def pontos_por_time(lista):
    '''Função que retorna um dicionario que informa o nome do time
       e o numero de pontos de cada rodada
       list(list, list, ...) -> dicionario '''
    lista =[[ time, time2,[ci,fi]],[ time2, time,[f,c]]]
    #Pontos jogo-ida
    if ci==fi:
        return (ci==1) and (fi==1)
    else ci>fi:
        return (ci==3) and (fi==0)
    else ci<fi:
        return (ci==0)and(fi==0)
    #Pontos jogo-volta
    if f==c:
        return (f==1)and(c==1)
    else f>c:
        return (f==3)and(c==0)
    else f<c:
        return (f==0)and(c==0)
    return dado_rodada{str(time): str(ci+c),str(time2):str(fi+f)}