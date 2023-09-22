def maiores(lista, n):
    '''Funcao que dada uma lista de numeros inteiros e um outro
    numero inteiro n, retorna outra lista que contenha todos os
    numeros da lista original maior que n'''
    
    lista.append(n)
    lista.sort()
    inicio_contagem = lista.index(n)
    contagem_maiores= lista[inicio_contagem+1:]

    return contagem_maiores