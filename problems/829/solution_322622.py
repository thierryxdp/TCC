def soma_h(n):
    "Retorne a soma o valor n dos números de 1 a n(inclusive) dividindo 1; int->float"
    l=list(range(1,n+1))
    r=0
    for i in l:
        r+=1/i
    return round(r,2)