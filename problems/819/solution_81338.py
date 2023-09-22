def filtraMultiplos(lista,n):
    '''
       Função que recebe uma lista de numeros(lista) e um numero inteiro (n) e
       retorna os elementos da lista que sao divisiveis de n;
       list, int -> list
    '''
    listanova=0
    i=0
    el=lista[i]
    while i<len(lista):
        if el%n==0:
            listanova = listanova + [el]
        i=i+1
    return listanova