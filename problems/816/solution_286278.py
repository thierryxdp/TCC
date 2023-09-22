numeros=[1,2,3,4,5,6,7,8,9,0]
n = 'n'

def maiores(numeros,lista):
    '''função que dada uma lista de números e determinado
    número inteiro n como entradas, retorna outra lista
    contendo os números da lista original maiores que n,
    ordenados do menor para o maior
    string -> string'''
    for numero in lista:
        if numero > n:
            lista.final.append(numero)