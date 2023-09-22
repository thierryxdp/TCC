def insere(lista_numero,n):
    '''insere um numero 'n' na posição correta de modo crescente. 
   list,int -> int'''
    new_lista = lista_numero + [n]
    return list.sort(new_lista)