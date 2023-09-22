def filtra_pares(tup)
	"""Esta funcao recebe uma tupla com 4 elementos, e retorna outra que contém
    apenas os elementos pares da primeira."""
    tupares=()
    if tup[0]%2==0:
        tupares=tupares+(tup[0],)
	if tup[1]%2==0:
		tupares=tupares+(tup[1],)
	if tup[2]%2==0:
		tupares=tupares+(tup[2],)
	if tup[3]%2==0:
		tupares=tupares+(tup[3],)
       return tupares