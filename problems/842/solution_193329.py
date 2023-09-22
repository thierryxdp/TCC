def pontos_por_time(time1,time2,t1,t2,ttime2,ttime1,tt2,tt1):
    """Função que retorna os nomes dos times e o número de pontos na fase"""
    """tupla-->tupla"""
    
    if t1>t2 and tt1>tt2: 
         return time1 , '6' , time2 , '0'
    elif t1==t2 and tt1>tt2:
         return time1 , '4' , time2 , '1'
    elif t1>t2 and tt1==tt2:
         return time1 , '4' , time2 , '1'
    elif t1==t2 and tt1==tt2:
         return time1 , '2' , time2 , '2'
    elif t1<t2 and tt1>tt2:
         return time1 , '3' , time2 , '3'
    elif t1>t2 and tt1<tt2:
         return time1 , '3' , time2 , '3'
    elif t1<t2 and tt1<tt2:
         return time1 , '0' , time2 , '6'