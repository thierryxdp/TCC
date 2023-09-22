def insere(lista_numero,n):
    """essa funçao recebe somente numeros inteiros,e retorna os numeros menor para maior"""
    a=lista_numero
    list.insert(a,0,n)
    list.sort(a)
    return a