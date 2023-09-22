def maiores(lista_inteiros, n):
    """A entrada é uma lista de números inteiros e um número
    inteiro, ambos descritos no parâmetro e o seu retorno é
    uma lista que inclui todos os elementos da primeira lista, mas 
    apenas os maiores que o número incluso no parâmetro n. Essa nova
    lista deve estar em ordem crescente."""
    #int, int -> int
    
    listanova = list.append(lista_inteiros, n)
    listanova.sort()
    index = list.index(listanova, n+1)
    del listanova[0:index]
   
    return listanova