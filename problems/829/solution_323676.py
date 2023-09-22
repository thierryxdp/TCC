import math
def soma_h(numero):
    ''' Função que pega o número de entrada e calcula a fórmula de H, e retorna o H
    int, int→float'''
    lista=list(range(1,numero+1))
    mmc=lista[0]
    lista2=[]
    soma=0
    for i in range(1, len(lista)):
        mmc= mmc*lista[i]//math.gcd(mmc,lista[i])
    for x in range(len(lista)):
        h=mmc/lista[x]
        lista2.append(h)
    for l in range(len(lista2)):
        soma= soma + lista2[l]
    soma= soma/mmc
    return round(soma,2)