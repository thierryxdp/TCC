def maiores(lista,n):
    """dada uma lista de int e um n int
retorna apenas a parte da lista que é
maior que n
ex: >>>([1,2,3,4,5],2) - [3,4,5]"""
    if list.count(lista,n) == 0: #verifica se tem o numero na lista, se for igual a 0, então não tem
        
        lista = lista + [n] #concatenar as listas
        list.sort(lista) #colocar em ordem crescente
        posicao = list.index(lista,n) #posição em que o numero estará
        
        return lista[1+posicao:] #pegando apenas o numeros maiores que ele

    else:
        list.sort(lista)
        posicao = list.index(lista,n) #posição em que o numero estará
        
        return lista[1+posicao:] #pegando apenas o numeros maiores que ele