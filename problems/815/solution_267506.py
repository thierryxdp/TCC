def insere(lista_numero,n):
    """Dado uma lista e um número inteiro como argumentos, a função 
    retorna a lista em ordem crescente da lista com o o número n incluso;
    lista,int->lista """
    
    lista=lista_numero+[n]
    list.sort(lista)
    return lista