#Start your python function here
def filtra_pares(tupla):
    """Receba uma tupla com quatro elementos inteiros como argumento, e retorne uma nova tupla 
    contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam;
    tuple -> tuple"""
    tupla_nova = ()
    if len(tupla) == 4:
        if tupla[0] % 2 == 0:
            tupla_nova += (tupla[0],)
        if tupla[1] % 2 == 0:
            tupla_nova += (tupla[1],)
        if tupla[2] % 2 == 0:
            tupla_nova += (tupla[2],)
        if tupla[3] % 2 == 0:
            tupla_nova += (tupla[3],)
	return tupla_nova