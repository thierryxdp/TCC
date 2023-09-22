def insere(lista_numero,n):
    '''insere um numero 'n' na posição correta de modo crescente. 
   list,int -> int'''
    new_lista = list.sort(lista_numero + n)
    return new_lista