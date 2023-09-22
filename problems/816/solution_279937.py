def maiores(ln,n):
    '''dado uma lista, retorna outra lista com todos os numeros
    da lista original menos n. list -> list'''
    ln = ln+[n]
    list.sort(ln)
    ln[0:n+1]=[]
    return ln