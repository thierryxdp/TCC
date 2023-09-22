def repetidos(lista):
    '''
       Função que recebe uma lista e retorna o numero de vezes que 
       um elemento é igual ao elemento anterior
       list -> int
    '''
    qnt=0
    i=1
    while i < len(lista):
        if lista[i]==lista[i-1]:
            qnt = qnt + 1
        i=i+1
    return qnt