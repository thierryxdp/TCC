def maiores(lista,n):
    """Função que, dada uma lista de números inteiros e um
    número inteiro n, retorna outra lista, que contenha todos
    os números da lista original maiores que n em ordem
    crescente.
    lista,int->lista"""
    lista2=[]
    for i in lista:
        if i > n:
            lista2.append(i)
            list.sort(lista2)
    return lista2