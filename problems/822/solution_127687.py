def repetidos(lstNum):
    '''
    Função que recebe uma lista numérica e retorna o
    número de vezes em que um elemento na lista é igual
    ao anterior.
    list -> int
    '''
    i= 0
    cont = 0
    while i <= (len(lstNum)-1):
        if lstNum[i] == lstNum[i-1]:
            cont += 1
        i += 1
        
        
    return cont