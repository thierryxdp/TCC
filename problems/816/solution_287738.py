def maiores(lista,n):
    """funcao que, dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista,
    que contem todos os numeros da lista original maiores que n, em ordem crescente"""
    lista2 = []
    if lista[0] > n:
        lista2 = lista2 + [lista[0],]
    if lista[1] > n:
        lista2 = lista2 + [lista[1],]
    if lista[2] > n:
        lista2 = lista2 + [lista[2],]
    if lista[3] > n:
        lista2 = lista2 + [lista[3],]
    if lista[4] > n:
        lista2 = lista2 + [lista[4],]
    if lista[5] > n:
        lista2 = lista2 + [lista[5],]
    if lista[6] > n:
        lista2 = lista2 + [lista[6],]
    if lista[7] > n:
        lista2 = lista2 + [lista[7],]
    if lista[8] > n:
        lista2 = lista2 + [lista[8],]
    return lista2