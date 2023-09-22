def insere([lista_numero],n):
    '''Função que dada uma lista ordenada de números e um número inteiro N, retorna N na posição correta de acordo om a organização)
    list, int -> list'''
    
    Lista_Num_nova = list.insert(lista_numero,0,n)
    
    return list.sorte(Lista_Num_nova)