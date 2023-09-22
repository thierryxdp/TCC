#Start your python function here

def filtra_pares(w,x,y,z):
    tupla1 = (w,x,y,z)
    if w%2 > 0:
        return tupla1 - w
    if x%2 > 0:
        return tupla1 - x
    if y%2 > 0:
        return tupla1 - y
    if z%2 > 0:
        return tupla1 - z
    else:
    	return tupla1