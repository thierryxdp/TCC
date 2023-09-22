#a função retorna o zeta de 1 para uma quantidade de numeros finita.
#int->float
def soma_h(n):
    x=1
    a=0
    lista=[]
    while n>=x:
        lista.append(x)
        x+=1
    for item in lista:
        a+=item^-1
    return(round(a,2))