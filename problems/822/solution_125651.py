def repetidos(listaN):
    '''
        função que recebe uma lista de inteiros e calcula quantas vezes um elemento
        é igual ao elemento anterior.
        list -> int
    '''
    i=0
    contador=0
    while i < len(listaN):
        if listaN[i] == listaN[i-1]:
            contador = contador+1
            if len(listaN)== 2 and listaN[0] == listaN[1]:
                return 1                
        i = i+1
    return contador