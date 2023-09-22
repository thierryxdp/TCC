def filtraMultiplos(listaO,n):
    '''
        Dada uma lista de inteiros e um numero n, retorna uma lista com
        todos os números da lista original que são divisíveis por n
        lista,int -> list
    '''
    i=0
    d=[]
    while i<len(listaO):
        if listaO[i]%n == 0:
            d = d + [listaO[i]]
        i=i+1
    return d