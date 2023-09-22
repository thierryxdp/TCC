def ordenada(lista):
    """Funcao que dada uma lista ordenada(crescente) de números inteiros e um número inteiro n, inclua n na posição correta, ou seja, de tal maneira que a lista continue ordenada.
    list -> list"""
    
    lista_cresc = lista[:]
    lista_decresc = lista[:]
    
    list.sort(lista_cresc)
    list.sort(lista_decresc)
    list.reverse(lista_decresc)
    
    if lista == lista_cresc:
        return (True, 'crescente')
    elif lista == lista_decresc:
        return(True,'decrescente')
    else:
        return (False, 'desordenada')
    
    [5,19,10110,-1,2]