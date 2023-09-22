def filtraMultiplos(lista,n):
    '''
       Função que recebe uma lista de numeros(lista) e um numero inteiro (n) e
       retorna os elementos da lista que sao divisiveis de n;
       list, int -> list
    '''
    listanova=[]
    i=0
    while i<len(lista):
        el=lista[i]
        if el%n==0:
            listanova = listanova + [el]
        i=i+1
    return listanova