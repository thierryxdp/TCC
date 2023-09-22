def repetidos ( listan: list)-> int:
    '''Retorna quantas vezes um elemento da lista é igual ao elemento
    anterior'''
    i = 1
    contador = 0
    while i < len(listan):
        if listan[i-1]== listan[i]:
            contador = contador + 1
        i = i +1
    return contador