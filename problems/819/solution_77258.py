def filtraMultiplos(lista_num,n):
    '''Esta função retorna elementos da lista inserida(lista_num) 
    que forem divisíveis pelo número (n) inserido.
    list,int -> list'''
    
    divisiveis=[]
    indice=0
    
    while indice<len(lista_num):
        if lista_num[indice]%n==0:
            list.append(divisiveis,lista_num[indice])
        indice = indice + 1
        
    return divisiveis