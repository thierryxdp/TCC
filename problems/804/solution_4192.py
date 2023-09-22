#Start your python function here
def filtra_pares (tupla):
	"""funcao que recebe elementos inteiros como parametro e retorna uma nova tupla contendo apenas os elementos pares da yupla original, na mesma ordem que se encontravam (filtragem).
    	tupla -> tupla"""
    pares = ()
    if tupla[0]%2==0:
		pares=pares+(tupla[0],)
    if tupla[1]%2==0:
		pares=pares+(tupla[1],)
    if tupla[2]%2==0:
		pares=pares+(tupla[2],)
    if tupla[3]%2==0:
		pares=pares+(tupla[3],)
		
        return pares