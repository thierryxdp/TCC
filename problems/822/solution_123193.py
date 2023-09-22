def repetidos(lista:list) ->int:
    '''Recebe uma lista de números e retorna o número de vezes que um 
    elemento da lista é igual ao anterior.'''
    i = 1
    repeticoes = 0
    while i<len(lista):
        if lista[i] == lista[i-1]:
        	repeticoes = repeticoes + 1
        i = i+1
    return repeticoes