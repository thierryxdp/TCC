def filtraMultiplos(lista,n):
    ''' funcao recebe uma lista e um numero(n) e retorna os
    numeros multiplos desse numero ques estao na lista. 
    list,int-->list'''
    lista=()
    proximo=0
    while lista[proximo]%2==0:
        list.apped(lista,lista[proximo])
        proximo= proximo+1
        return lista