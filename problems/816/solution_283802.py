def maiores(lista,n):
    '''
       Função que recebe uma lista contendo uma ordem numérica aleatória 
       e um número (n) inteiro. Retorna a lista original contendo apenas 
       os números que são maiores que (n).
       list,int --> list
    '''
   
    lista_maior = lista + [n]
    lista_maior.sort()
    del (lista_maior[0:n])

    if lista_maior.index(n) == lista_maior[0]:

     return lista_maior[1:]

    elif n not in lista:

     return lista_maior[n:]

    elif n in lista:

     return lista_maior[n:]

    else:

     return lista_maior[n:]