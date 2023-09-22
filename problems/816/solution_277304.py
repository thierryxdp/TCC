def maiores (lista, n):
     ###Função maiores que, dada uma lista de números inteiros e um número inteiro n###
     ###Retorna outra lista, que contenha todos os números da lista original maiores que n###
     ###list, int -> list###
    
    if n in lista:
        L = list.index (lista,n)
        return lista ( n + 1 :)
    
    if n not in lista:
        list.append (n)
        list.sort (lista)
        L1 = list.index (lista, n)
        return lista (L1+1:)