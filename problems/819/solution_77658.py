def filtraMultiplos(l,n):
    '''Função que retorna os multiplos de n dado uma lista de 
    numeros (l). list,int -> list.'''
    lista=[]
    i = 0
    while len(l) > i:
        if l[i]%n == 0:
            lista = lista + [l[i]]
        i = i + 1
    return lista