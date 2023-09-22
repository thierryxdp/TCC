def insere(lista_numero,n):
    """Retorna uma lista com o inteiro n inserido na posição correta.
    lista, int --> lista"""
    
    nova_lista = list.sort(lista_numero)
    
    if n in lista_numero:
        index = list.index(lista_numero,n)
        list.insert(lista_numero, index,n)
        return lista_numero
    else:
        index_anterior = list.index(lista_numero,(n-1))
        index_posterior = list.index(lista_numero,(n+1))
        novo_index = index_anterior + 1
        list.insert(lista_numero,novo_index,n)
        
       	return lista_numero