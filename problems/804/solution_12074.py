#Start your python function here

def filtra_pares(elements):
    tupla1 = ()
    if elements[0]%2 == 0:
        tupla1 + (elements[0],)
    elif elements[1]%2 == 0:
        tupla1 + (elements[1],)
    elif elements[2]%2 == 0:
        tupla1 + (elements[2],)
    elif elements[3]%2 == 0:
        tupla1 + (elements[3],)
    else:
    	return tupla1