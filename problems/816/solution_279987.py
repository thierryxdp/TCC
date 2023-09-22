def maiores (lista, numero):
        
    """funcao que dada uma lista e um numero, retorn uma outra lista com todos os numeros da lista original maiores que o numero dado
    list, int -> list"""
    numerosdados = lista[:]
    if (n not in numerosdados):
        
        numerosdados.append(numero)
        numerosdados.sort(reverse = True)
    l = numerosdados.index(numero)
    return sorted(numeros[:1])