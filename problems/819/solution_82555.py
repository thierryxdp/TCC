def filtraMultiplos(lista,n):
    '''funcao que recebe uma lista de numeros e um numero n e retorna uma lista com os multiplos de n
    list,int->list'''
    multiplos=()
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
                       multiplos=multiplos+(list.extend(lista)[proximo],)
        proximo=proximo+1
    return multiplos