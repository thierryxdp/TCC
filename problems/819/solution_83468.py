def filtraMultiplos(lista,n):
    
    '''Função que recebe como entrada uma lista de números e um número, e retorna outra lista contendo todos os elementos da lista original que forem divisíveis por n;
       list,int->list'''
    proximo = 0
    m = []
    while proximo<len(lista):
        if lista[proximo]%n==0:
            m = m + [lista[proximo]]
        proximo = proximo + 1
    return m