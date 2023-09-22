def filtraMultiplos(lista,n):
    '''Função que recebe como entrada uma lists de números e um
    número, e retorna outra lista contendo todos os elementos da
    lista original que forem divisíveis por n
    lista=list->list'''
    mult=[]
    y=0
    while y<len(lista):
        if lista[y]%n==0:
            mult=mult+[lista[y]]
        y=y+1
    return multiplos