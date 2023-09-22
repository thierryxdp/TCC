def insere(lista_numero, n):
    
    ''' Função que, dada uma lista de números
        em ordem crescente e um número inteiro,
        inclua tal número em uma posição que 
        mantenha a lista ordenada.
        list, int -> list '''
    
    lista_nova = lista_numero + [n,]
    
    list.sort(lista_nova)
    
    return lista_nova