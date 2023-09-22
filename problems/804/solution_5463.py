def filtra_pares(a,b,c,d):
    '''Função que retorna uma nova tupla contendo apenas
    os elemetos pares da tupla original, na mesma ordem em que
    se encontravam.
    a=int,b=int,c=int,d=int->tuple'''
    lista = []
 	if tupla[a] % 2 == 0:
       lista.append(tupla[a])
    if tupla[b] % 2 == 0:
       lista.append(tupla[b])
    if tupla[c] % 2 == 0:
       lista.append(tupla[c])
    if tupla[d] % 2 == 0:
       lista.append(tupla[d])       
    return tuple(lista)