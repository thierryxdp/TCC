def insere(lista_numero,n):
    """função que dada uma lista em ordem crescente
    e um numero, adiciona o numero a lista
    list-> int -> list"""
    n=[n,]
    list= [[lista]+ [n]]
    return sorted(lista+ n,reverse=False)