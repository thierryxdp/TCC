def pontos_por_time (x):
    '''funçao que recebe o resultado de dois jogos e retorna quantos pontos tem cada time;
str,str->str'''
    jogo1 , jogo2= x
    
    timea, timeb,saldojogo1 = jogo1
    timeb, timea,saldojogo2 = jogo1
    
    a = 0
    b = 0

    if saldojogo1[0]>saldojogo1[1]:
        a= a +3
    elif saldojogo1[0]<saldojogo1[1]:
        b = b +3
    else:
        a= a +1
        b = b+1

    if saldojogo2[0]>saldojogo2[1]:
        a= a +3
    elif saldojogo2[0]<saldojogo2[1]:
        b = b +3
    else:
        a= a +1
        b = b+1

    

    return int(timea)+int(:)+int(a)+int(timeb)+int(:)+int(b)