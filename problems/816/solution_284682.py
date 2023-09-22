def maiores(lista,n):
    """Função que, dada uma lista de numeros inteiros e um
    número inteiro n, retorna outra lista que contenha todos
    os números da lista original maiores que n, ordenados em
    ordem crescente."""
    lista2=[]
    for i in lista:
        if lista[i]>n:
            return lista2.append(i)