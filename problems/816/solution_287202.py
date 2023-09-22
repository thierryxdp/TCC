def maiores (a,n):
    """Função que recebe uma lista de números inteiros e um
    número inteiro n e retorna outra lista que contem todos
    os numeros da lista original maiores que n ordenados em
    ordem crescente
    list, int -> list"""
    list.sort(a)
    lista=[]
    for i in a:
        if i>n:
            lista.append(i)
    return lista