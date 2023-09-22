def filtraMultiplos(lista,n):
    '''Função que recebe como entrada uma lists de números e um
    número, e retorna outra lista contendo todos os elementos da
    lista original que forem divisíveis por n
    lista=list->list'''
    multiplos=[]
    y=0
    while x<len(lista):
        if lista[x]%n==0:
            multiplos=multiplos+[lista[y]]
        x=x+1
    return multiplos