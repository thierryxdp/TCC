def insere(lista_numero,n):
    '''função que retorna uma lista ordenada de números inteiros com um
    número 'n' incluso em orden crescente.
    lista, int -> lista'''
    
    nova_lista = list.insert(lista_numero,0,n)
    
    return nova_lista