def acima_da_media(notas):
    ''''''
    n = 6   
    numero = notas
    list.sort(notas)
    if notas[0] < n:
        return [i for i in notas if i >= n]
    else:
        return lista_numero
'''
def maiores(lista_numero,n):
    Uma função dada uma lista de numeros inteiros e um numero inteiro n,
       e retorna outra lista, que contenha todos os numeros da lista original 
       maiores que n ordenados em ordem crescente. list[int],int -> list[int]
    numero = lista_numero
    list.sort(lista_numero)
    if lista_numero[0] < n:
        return [i for i in lista_numero if i > n]
    else:
        return lista_numero'''