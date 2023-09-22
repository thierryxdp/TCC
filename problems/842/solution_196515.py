#Essa função receberá uma lista de 2 lementos e retornará os pontos por time.
def pontos_por_time(a):
    b=a[0]
    c=b[2]
    d=a[1]
    e=d[2]
    if c[0]>c[1] and d[0]>d[1]:
        return(f'{b[0]},:6,{b[1]}:0')