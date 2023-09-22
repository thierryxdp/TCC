def filtraMultiplos(lista,n):
    '''filtraMultiplos recebe uma lista valor inteiro e devolve uma tuble
    determina os multiplos de n numa determinada lista 
    list, int --> tuble'''
    resposta=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            list.append(resposta,lista[proximo])
        proximo=proximo+1
    return resposta