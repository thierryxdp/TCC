def maiores(lista,n):
    '''
       Função que recebe uma lista e um número n e retorna outra lista
       com todos os numeros da lista original maiores que n ordenados em ordem crescente
       list, int -> list
    '''
    
    list.insert(lista,1,n)
    lista.sort()
    posicao=list.index(lista,n)
  
    
    
    return lista[posicao+1:]