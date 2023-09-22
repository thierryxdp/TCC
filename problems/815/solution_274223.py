def insere (lista_numero,n):
    ''' dada uma lista de números crescente e um número n,
    retorna o número na lista na posição certa
    list,int -> list'''
    
    concatena = lista_numero + [n]
    list.sort(concatena)
    return concatena