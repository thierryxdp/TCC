#int->float
def soma_h(N):
    #essa função define o H como 0 e n como 1
    H=0
    n=1
    #utilizo a Função For para achar o valor somado com o escopo indo de 1 até N
    for n in range(1,N+1):
        H+=1/n
        n+=1
    return round(H,2)