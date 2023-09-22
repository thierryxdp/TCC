def insere(lista,n):
    """funcao que dada uma lista de numeros int e tal numero n int, retorna
    na posicao posicao correta da lista. list,int-> list."""
    list.sort(lista)
    list.extend(lista,[n])
    list.sort(lista)
    return lista