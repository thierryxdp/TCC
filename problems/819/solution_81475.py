def filtraMultiplos(lista,n):
    ''' Função que filtra múltiplos de um número (n). Recebe 
        como entrada uma lista de números(lista) e um número(n)
        e retorna outra lista contendo todos os elementos da
        lista original que forem divisíveis por n. 
        : param lista: list
        : param n: int
        : return: list
    '''
    variavel=0
    listaA=[]
    while variavel<len(lista):
        if lista[variavel]%n==0:
            list.append(listaA,lista[variavel])
        variavel=variavel+1
    return listaA