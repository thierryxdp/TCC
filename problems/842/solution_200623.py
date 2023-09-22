def pontos_por_time(lista):
    '''Função que retorna um dicionario que informa o nome do time
       e o numero de pontos de cada rodada
       list(list[str, str],list[int,int])-> dict'''
    ci=lista[0][2][0]
    fi=lista[0][2][1]
    c=lista[1][2][0]
    f=lista[1][2][1]
    time=lista[0][0]
    time2=lista[0][1]
    lista =[[time,time2,[ci,fi]],[time2,time,[f,c]]]
    #Pontos jogo-ida
    if ci==fi:
        return 'empate'
    elif ci>fi:
        return 'vitoria'
    elif ci<fi:
        return 'vitoria2'
    #Pontos jogo-volta
    if f==c:
        return 'empate'
    elif f>c:
        return 'vitoria2'
    elif f<c:
        return 'vitoria'
    '''if (ci==fi) == ''empate:
        return 1
    else ci
    'vitoria1'=3
    'vitoria2'=3'''
    
    dado_rodada = {time:(ci+c), time2:(fi+f)}
    return dado_rodada