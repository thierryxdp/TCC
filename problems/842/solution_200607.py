def pontos_por_time(lista):
    '''Função que retorna um dicionario que informa o nome do time
       e o numero de pontos de cada rodada
       list(list[str, str],list[int,int])-> dict'''
    '''lista =[[time,time2,[ci,fi]],[time2,time,[f,c]]]'''
    ci=lista[0][2][0]
    fi=lista[0][2][1]
    c=lista[1][2][0]
    f=lista[1][2][1]
    time=lista[0][0]
    time2=lista[0][1]
    #Pontos jogo-ida
    if ci==fi:
        return (ci==1) and (fi==1)
    elif ci>fi:
        return (ci==3) and (fi==0)
    elif ci<fi:
        return (ci==0)and(fi==0)
    #Pontos jogo-volta
    if f==c:
        return (f==1)and(c==1)
    elif f>c:
        return (f==3)and(c==0)
    elif f<c:
        return (f==0)and(c==0)
    dado_rodada = {time:(ci+c), time2:(fi+f)}
    return dado_rodada