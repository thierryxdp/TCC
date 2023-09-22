def pontos_por_time(lista):
    '''Função que retorna um dicionario que informa o nome do time
       e o numero de pontos de cada rodada
       list(list[str, str],list[int,int])-> dict'''
    lista =[[TIME,TIME2,[xi,yi]],[time2,time,[y,x]]]
    ci=lista.index(xi)
    fi=lista.index(yi)
    c=lista.index(x)
    f=lista.index(y)
    time=lista.index(time)
    time2=lista.index(time2)
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