def maiores (inteiros,n):
    '''retorna outra lista com os numeros da original em ordem crescente maiores que n'''
    '''list,int -> list'''
    
    
    list.append(inteiros,n)
    crescente = sorted (inteiros)
    posicao = list.index(inteiros,n)
    lista = crescente[posicao:]
    lista1= list.remove(lista,n)
    
    return lista1