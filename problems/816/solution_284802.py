def maiores(lista, n):
    '''função que recebe uma lista de números e um número n e retorna
    outra lista contendo todos os números da lista original maiores que
    n ordenados em ordem crescente.
    entrada:lista,int
    saída:lista'''
    
    if n<len(lista):
        return lista[:n]