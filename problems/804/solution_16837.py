def filtra_pares(tupla):
    '''
Função que receba uma tupla de quatro elementos inteiros
como parâmetro, e retorne uma nova tupla contendo apenas
os elementos pares da tupla original, na mesma ordem em que
se encontravam.
tupla -> tupla>
	'''
    tupla4Elem = ()
    if tupla[0]%2 == 0:
        tupla4Elem = tupla4Elem + (tupla[0],)
    if tupla[1]%2 == 0:
        tupla4Elem = tupla4Elem + (tupla[1],)
    if tupla[2]%2 == 0:
        tupla4Elem = tupla4Elem + (tupla[2],)
    if tupla[3]%2 == 0:
        tupla4Elem = tupla4Elem + (tupla[3],)
    return tupla4Elem