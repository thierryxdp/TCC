#Start your python function here
def pontos_por_time(R1):
    ''' Função que calcula a pontuação de cada time, dados os valores
    de entrada do jogo de ida e volta, no formato 
    ([["time1","time2",["a","b"]],["time2","time1",[x,y]]])'''
    '''list -> dict'''
    time1=R1[0][0]
    time2=R1[0][1]
    a=R1[0][2][0]
    b=R1[0][2][1]
    x=R1[1][2][0]
    y=R1[1][2][1]
    n=0
    m=0 
    R1=[[str(time1),str(time2)],[int(a),int(b)],[[str(time2),str(time1)],[int(x),int(y)]]]
    if (int(a)==int(b)):
        n+=1
        m+=1
    if (int(x)==int(y)):
        n+=1
        m+=1
    if (int(a)>int(b)):
        n+=3
        m+=0
    if (int(a)<int(b)):
        n+=0
        m+=3
    if(int(x)>int(y)):
        n+=0
        m+=3
    if(int(x)<int(y)):
        n+=3
        m+=0
    Dicionario=({str(time1): n,str(time2): m})
    return Dicionario