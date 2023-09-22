def maiores(lista,n):
    """Função que retorna uma nova lista contendo apenas os números da lista 
    original maiores que n. list[int],int->list"""
   
    if n in lista:
        list.sort(lista)
        a1 = list.index(lista,n)
        return lista[a1+1]