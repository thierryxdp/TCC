def repetidos (listaNum):
    '''
    retorna a quantidade de vezes que um numero 
    foi repetido antes
    list -> int
    '''
    i=0
    soma = 0
    while i < len(listaNum)-1:
        if listaNum[i] == listaNum[i+1]:
            soma = soma +1
        i = i+1
    return soma