#Start your python function here
def filtra_pares(tupla):
    result = 0
    if tupla[0]%2 == 0:
    	result = tupla
	if tupla[1]%2 == 0:
    	result = result, tupla[1]
	if tupla[2]%2 == 0:
    	result= result, tupla[2]
	if tupla[3]%2 == 0:
    	result= result, tupla[3]
    return result