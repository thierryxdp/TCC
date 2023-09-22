def maiores(lista_numeros, n):
     """ Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n;
         list -> list"""
        y = lista_numeros + [n]
        list.sort(y)
        indice = list.index(y,n)
        lista_nova = lista_nova[indice: ]
        return lista_nova