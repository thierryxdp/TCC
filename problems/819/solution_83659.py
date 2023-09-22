def filtraMultiplos (x,n):
    
    '''
    função que recebe uma lista (x) e filtra os números que são divisiveis por "n", o retorno 
    será uma outra lista contendo apenas os elementos da lista original que forem divisíveis 
    por "n".
    '''
    listaMul=[]
    proximo=0
    while proximo<len(x):
        if x[proximo]%n==0:
            listaMul= listaMul+[x[proximo]]
        proximo=proximo+1
    return listaMul