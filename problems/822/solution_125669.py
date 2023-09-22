def repetidos(lista):
    '''dado uma lista de números, determina a quantidade de vezes
    que um elemento foi igual ao elemento anterior
    list -> list '''
    
    i = 1
    repeticoes = 0
    while i < len(lista):
    	if lista[i] == lista[i - 1]:
          	repeticoes = repeticoes + 1
        i = i + 1
    return repeticoes