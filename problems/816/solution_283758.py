def maiores(lista,n):
    '''
       Função que recebe uma lista contendo uma ordem numérica aleatória 
       e um número (n) inteiro. Retorna a lista original contendo apenas 
       os números que são maiores que (n).
       list,int --> list
    '''
   
    lista_maior = lista + [n]
    lista_maior.sort()

    if lista_maior.index(n) < lista_maior[1]:
     return lista_maior[1:]
    
    else:

     return lista_maior[n:]