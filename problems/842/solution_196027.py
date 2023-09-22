def pontos_por_time(k):
    k =[['time1','time2',[a,b]],['time2','time1',[c,d]]]
    (a>b)=(b>a) = 3
    (a=b) = 1
    (a<b)=(b<a) = 0
    (c>d)=(d>c) = 3
    (c=d)=(d=c) = 1
    (c<d)=(d<c) = 0
    return {"time1":(a+d),"time2":(b+c)}