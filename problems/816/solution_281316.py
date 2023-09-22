def maiores(lista_numeros, n):
     """ Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n;
         list -> list"""
        lista_nova = lista_numeros + [n]
        list.sort(lista_nova)
        indice = list.index(lista_nova,n)
        lista_nova = lista_nova[indice: ]
        return lista_nova