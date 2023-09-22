def insere(lista_numero:list,n:int)-> list:
    """Dados uma lista crescente de números inteiros
    (lista_numero) e um número inteiro n, a função inclui 'n'
    na lista mantendo sua forma ordenada."""
    
    list.append(lista_numero,n)
    list.sort(lista_numero) 
    
    return lista_numero