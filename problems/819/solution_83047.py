def filtraMultiplos(lista,n):
    ''' essa função tem como entrada uma lista e um numero, e  retorna uma lista com os numeros da lista original só que com os numeros divisiveis por n'''
    i=0
    multiplos=[]
    while i<len(lista):
        if i % n ==0:
            return i