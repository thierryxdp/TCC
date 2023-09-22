def filtraMultiplos(lista,n):
    '''Função que filtra todos os multiplos do número n,
    dando como entrada uma lista e um número n e retornando
    uma lista com os números divisíveis por n.
    list, int -> list'''
    
    multiplos=[]
    proximo = 0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            multiplos=multiplos+(lista[proximo],)
        proximo=proximo+1
    return multiplos