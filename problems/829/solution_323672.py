import math
def soma_h(numero):
	lista=list(range(1,numero+1))
    mmc=lista[0]
    for i in range(1, len(lista)):
        mmc= mmc*lista[i]//math.gcd(mmc,lista[i])
        h=lista[i]/mmc
    return h