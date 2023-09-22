def soma_h(N):
    'retorna a media dos n termos;int---float'
    x=1
    h=0
    while x<=n:
        h+=1/x
        x+=1
    return round(h,2)