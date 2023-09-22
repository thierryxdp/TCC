def filtraMultiplos(l,n):
    """Função que dados uma lista e um número, retornam quantos números da lista são divisíveis pelo número n
       list,int->list"""
    multiplos= []
    proximo=0
    while proximo < len(l):
        if l[proximo]%n==0:
            multiplos= multiplos+[l[proximo],]
            proximo= proximo + 1
    return multiplos