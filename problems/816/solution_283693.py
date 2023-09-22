def maiores(lista,n):
    '''
       Função que recebe uma lista contendo uma ordem numérica aleatória 
       e um número (n) inteiro. Retorna a lista original contendo apenas 
       os números que são maiores que (n).
       list,int --> list
    '''
        lista_maior = lista + [num]
        lista_maior.sort()
        del (lista_maior[0:num])
        
        return lista_maior