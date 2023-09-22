def repetidos(listaN):
    '''retorna o numero de vezes que um elemento i de uma lista é igual ao elemento anterior
    list -> int'''
    i = 1
    counter = 0
    while i < len(listaN):
        if (listaN[i] == listaN[i-1]):
            counter = counter + 1
		i = i+1
    return counter