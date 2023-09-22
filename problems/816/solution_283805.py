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
    del (lista_maior[0:num])

    if lista_maior.index(num) == lista_maior[0]:

     return lista_maior[1:]

    else:

     return lista_maior[num:]