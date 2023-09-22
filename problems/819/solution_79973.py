def filtraMultiplos(lista,n):
    '''
       Função que recebe uma lista de numeros(lista) e um numero inteiro (n) e
       retorna os elementos da lista que sao divisiveis de n;
       list, int -> list
    '''
    lista.insert(0,0)
    i=0
    x=lista[i]
    while x in lista:
        if x%n==0:
            listanova=[x]
        i=i+1
    del listanova[0]    
    return listanova