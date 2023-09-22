def insere(lista_numero,n):
    """Retorne a lista com de entrada com o parâmetro n na posição correta(crescente)"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista_numero,n):
    """Retorne uma lista que dada a lista de entrada, retorne os números da lista original maiores que n, em ordem crescente"""
    novo = lista_numero.index(n)
    maioresN = lista_numero[novo:]
    list.remove(maioresN,n)
    return maioresN