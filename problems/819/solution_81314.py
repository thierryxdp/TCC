def filtraMultiplos(lista,n):
    '''
       Função que recebe uma lista de numeros(lista) e um numero inteiro (n) e
       retorna os elementos da lista que sao divisiveis de n;
       list, int -> list
    '''
    i=0
    el=lista[i]
    listanova=[]
    while el in lista: 
        el%n==0
        listanova=[el,]
        i=i+1   
    return listanova