def maiores(lista,n):
    '''funcao que insere um numero n na posicao correta e retorna outra lista somente com os maiores que n''' 
    lista.append(n)
    list.sort(lista)
    m=lista.index(n)
    del(lista[:m+1])
    return lista