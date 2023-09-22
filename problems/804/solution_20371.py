def filtra_pares(tup):
    """Esta funcao recebe uma tupla contendo quatro parametros, e retorna uma
    nova tupla contendo apenas elementos pares da tupla inicial."""
    tupaux=()
    if tup[0]%2==0:
        tupaux=tupaux+tup[0]
	if tup[1]%2==0:
        tupaux=tupaux+tup[1]
	if tup[2]%2==0:
        tupaux=tupaux+tup[2]
    if tup[3]%2==0:
    	tupaux=tupaux+tup[3]