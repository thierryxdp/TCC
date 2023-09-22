def pontos_por_time(lista0):
    """Função que retorna um dicionário com o time e seu total de pontos< list,list ->dicionário."""
    jogo1=lista0[0]
    jogo2=lista0[1]
    Time1= jogo1[0]
    Time2= jogo1[1]
    gols1= jogo1[2]
    Time11=gols1[0]
    Time21=gols1[1]
    gols2=jogo2[2]
    Time12=gols2[1]
    Time22=gols2[0]
    if Time11==Time21==0 and Time12==Time22==0:
        tabela = {Time1: '2 pontos', Time2: '2 pontos'}
        return tabela
    if Time11==Time21==0 and Time12>Time22:
        tabela = {Time1: '4 pontos', Time2: '1 ponto'}
        return tabela
    if Time11==Time21==0 and Time12<Time22:
        tabela = {Time1: '1 ponto', Time2: '4 pontos'}
        return tabela
    if Time11>Time21 and Time12==Time22==0:
        tabela = {Time1: 4, Time2: '1 ponto'}
        return tabela
    if Time11<Time21 and Time12==Time22==0:
        tabela = {Time1: '1 pontos', Time2: '4 ponto'}
        return tabela
    if Time11>Time21 and Time12>Time22:
        tabela = {Time1: '6 pontos', Time2: '0 pontos'}
        return tabela
    if  Time11>Time21 and Time12<Time22:
        tabela = {Time1: '3 pontos', Time2: '3 pontos'}
        return tabela
    if Time11<Time21 and Time12>Time22:
        tabela = {Time1: '3 pontos', Time2: '3 pontos'}
        return tabela
    if Time11>Time21 and Time12>Time22:
        tabela = {Time1: '0 pontos', Time2: '1 pontos'}
        return tabela