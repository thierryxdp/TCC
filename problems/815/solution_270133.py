def insere(lista_numero,n):
    '''insere um numero 'n' na posição correta de modo crescente. 
   list,int -> int'''
    lista_numero = lista_numero+[n]
    list.sort(lista_numero)
    return lista_numero