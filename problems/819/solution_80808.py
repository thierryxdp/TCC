def filtraMultiplos(lista,n):
    ''' funcao recebe uma lista e um numero(n) e retorna os
    numeros multiplos desse numero ques estao na lista. 
    list,int-->list'''
    lista1=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            list.append(lista1,lista[proximo])
        proximo= proximo +1
    return lista1