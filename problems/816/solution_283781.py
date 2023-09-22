def maiores(lista_inteiros, n):
    """A entrada é uma lista de números inteiros e um número
    inteiro, ambos descritos no parâmetro e o seu retorno é
    uma lista que inclui todos os elementos da primeira lista, mas 
    apenas os maiores que o número incluso no parâmetro n. Essa nova
    lista deve estar em ordem crescente."""
    #int, int -> int
    
    lista_nova = list.append(lista_inteiros, n)
    lista_nova.sort()
    index = list.index(n+1)
    list.remove(lista_nova, lista_nova[:index])
   
    return lista_nova[index+1]