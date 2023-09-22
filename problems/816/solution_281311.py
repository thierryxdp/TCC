def maiores(lista_numeros,n):
     """ Função que dada uma lista de números inteiros e um número inteiro n, retorna outra lista, que contenha todos os números da lista original maiores que n;
         list -> list"""
        lista = lista_numeros+[n]
        lista_nova = str.sort(lista)
        indice = list.index(lista,n)
        lista_nova = lista_nova[indice: ]
        return lista_nova