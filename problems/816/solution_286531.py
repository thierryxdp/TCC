def maiores(a,n):
    '''
       funcao que dada uma lista de numeros inteiros mais outro inteiro
       e retorna outra lista com os elementos da lista original
       maiores que o inteiro acrescentado
    ''' 
    list.append(a,n)
    list.sort(a)
    z=len(a)
    y=list.index(a,n)
    return a[y+1:z]