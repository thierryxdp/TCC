def maiores(lista,n):
    """Pede uma lista de números inteiros e um número inteiro n.
    Retorna uma lista que contenha os numeros da lista original
    maiores que n
    list,int->list"""
    #Insere o número n na lista passada no input
    #e ordena em ordem crescente
    lista.append(n)
    lista.sort()
    #Determina onde o número n aparece pela 1a vez,
    #quantas vezes ele é repetido, e fatia a lista
    corte=lista.index(n)
    contagem=lista.count(n)
    return lista[corte+contagem:]