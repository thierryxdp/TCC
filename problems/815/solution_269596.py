def insere(lista_numero,n):
    '''Dada uma lista ordenada de números de forma 
    crescente(lista_numero) e um número inteiro (n), essa
    função retorna uma nova lista acrescentada do número (n)
    ainda ordenada.
    list(float) -> list'''
    
    list.insert(lista_numero,1,n)
    list.sort(lista_numero)
    
    return lista_numero