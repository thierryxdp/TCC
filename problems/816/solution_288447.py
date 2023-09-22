def  maiores (*n):
    '''
    Função que dada uma lista de numeros inteiros e
    um numero inteiro n, 
    retorna uma lista com todos os
    elementos maiores que (n), ordenados em ordem crescente
    list, int --> list.
    '''
    nova_lista=n[0]
    args= n[1]
    nova_lista.append(args)
    if  max(nova_lista) ==  args:
        return []
    else :
        lista_decrescente  =  sorted(nova_lista,reverse = True )
        index_n  =  lista_decrescente.index(args)
        return  sorted( lista_decrescente [: index_n ])