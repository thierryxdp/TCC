def maiores(lista_numeros, n):
    '''
    função que recebe uma lista de números inteiros e um 
    número inteiro. A função retorna outra lista que tenha
    todos os números da lista parâmetro maiores que n 
    ordenados em ordem crescente
    '''
   	
    list.append(lista_numeros, n)
    list.sort(lista_numeros)
    numbers = lista_numeros
	maiores = [number for number in numbers if number > n]
    return maiores