def maiores(lista_inteiros,n):
    '''função que dada uma lista de numeros inteiros, insere o numero n na posição correta
    e retorna outra lista somente com on numeros maiores que n'''
    lista_inteiros.append(n)
    list.sort(lista_inteiros)
    m=lista_inteiros.index(n)
    
    if max(lista_inteiros)>n:
        lista_inteiros=del(lista_inteiros[:m+1])
    else:
        lista_inteiros=[]
    return lista_inteiros