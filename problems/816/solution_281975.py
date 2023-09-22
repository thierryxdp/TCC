def maiores (lista, n):
    '''
       Função que recebe uma lista de numero inteiros (lista)
       e um numero inteiro (n) e retorna outra lista, 
       contendo todos os numeros da lista original maiores
       que n, ordenados em ordem crescente;
       list, int -> list
    '''
    lista.sort()
    lista2 = [lista[0:]>n]
    lista.remove(lista2)
    return lista