def insere(lista_numero,n):
    '''insere um numero 'n' na posição correta de modo crescente. 
   list,int -> int'''
    n = list.sort(lista_numero + [n])
    return n