def filtraMultiplos(lista,n):
    '''
       Função que recebe uma lista de numeros(lista) e um numero inteiro (n) e
       retorna os elementos da lista que sao divisiveis de n;
       list, int -> list
    '''
    listanova=[]
    i=0
    #el=lista[i]
    while i<len(lista): 
        if lista[i]%n==0:
            listanova = listanova + lista[i]
        i=i+1   
    return listanova