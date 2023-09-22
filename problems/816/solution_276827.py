def maiores(lista, n):
    
#retorna uma lista que contanha todos os números da lista original maiores que n, dado a lista original e o valor de n

    lista.append(n)
    lista.sort()
    posicao = lista.index(n)

    return lista[posicao+lista.count(n):]