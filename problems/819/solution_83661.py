def filtraMultiplos (y,n):
    
    '''
    função que recebe uma lista (x) e filtra os números que são divisiveis por "n", o retorno 
    será uma outra lista contendo apenas os elementos da lista original que forem divisíveis 
    por "n".
    '''
    lista=[]
    div=0
    while div<len(y):
        if y[div]%n==0:
            lista= lista+[y[div]]
        div = div+1
    return lista