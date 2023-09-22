def filtra_pares(tupla):
    '''Função que retorna uma nova tupla contendo apenas
    os elemetos pares da tupla original, na mesma ordem em que
    se encontravam.
    a=int,b=int,c=int,d=int->tuple'''
    lista = []
 	if tupla[0] % 2 == 0:
       		lista.append(tupla[0])
    if tupla[1] % 2 == 0:
       		lista.append(tupla[1])
    if tupla[2] % 2 == 0:
       		lista.append(tupla[2])
    if tupla[3] % 2 == 0:
       		lista.append(tupla[3])       
    return tuple(lista)