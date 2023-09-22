def insere(lista_numero,n):
    """Funçao que dada uma lista ordenada(crescente) de numeros inteiros
    e um numero inteir(n),retorne o n na posiçao correta e ordenada"""
    list.sort([lista_numero])
    return str.join(n,lista_numero)