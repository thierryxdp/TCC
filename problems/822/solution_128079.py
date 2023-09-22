def repetidos(numeros):
    '''
       Dada uma lista de números a função retorna quantas 
       vezes um elemento é igual ao elemento anterior
       list -> int
    '''
    i=0
    repeticoes=0
    while i<len(numeros):
        if numeros[i]==numeros[i-1]:
            repeticoes=repeticoes+1
        i=i+1
    return repeticoes