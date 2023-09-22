def insere(lista_numero,n):
    '''insere um numero 'n' na posição correta de modo crescente. 
   list,int -> int'''
    list.sort(lista_numero+[n])
    return lista_numero