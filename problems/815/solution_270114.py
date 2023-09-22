def insere(lista_numero,n):
    '''insere um numero 'n' na posição correta de modo crescente. 
   list,int -> int'''
    n = lista_numero + [n]
    return list.sort(n)