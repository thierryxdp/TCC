#Start your python function here
def filtra_pares(t):
	''' retorna os numeros pares de uma tupla
    tupla=>tupla'''
    tupla_nova= tuple()
    if t[0]%2== 0:
    	tupla_nova=tupla_nova+(t[0],)
	if t[1]%2== 0:
    	tupla_nova=tupla_nova+(t[1],)
    if t[2]%2== 0:
    	tupla_nova=tupla_nova+(t[2],)
    if t[3]%2== 0:
    	tupla_nova=tupla_nova+(t[3],)
    return tupla_nova