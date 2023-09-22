def insere(lista_numero : list, n :int) -> int:
    """ Dada uma lista ordenada(crescente) de números inteiros
    adiciona o número inteiro n nessa lista de modo que a ordem 
    crescente se mantenha. Retorna a nova lista."""
    
    list.append(lista_numero,n)
    list.sort(lista_numero)
    
    return lista_numero