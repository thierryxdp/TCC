def insere(lista_numero,n):
    """função que dada uma lista em ordem crescente
    e um numero, adiciona o numero a lista
    list-> int -> list"""
    n=[n,]
    list= [[lista_numero]+ [n]]
    return sorted(lista_numero+ n,reverse=False)