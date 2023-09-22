def maiores(lista,n):
    '''
       Função que recebe uma lista contendo uma ordem numérica aleatória 
       e um número (n) inteiro. Retorna a lista original contendo apenas 
       os números que são maiores que (n).
       list,int --> list
    '''
    num = n
    lista_maior = lista + [num]
    lista_maior.sort()


    return lista_maior[num:]