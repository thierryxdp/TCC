def insere(lista_numero,n):
    '''
       função que recebe uma lista de numeros inteiros e um dado numero (n) 
       e inclui (n) na posição ordenada da lista organizada em ordem crescente
       list,int --> list
    '''
    
    lista_numero.append(n)
    lista_numero.sort()
    
    return lista_numero