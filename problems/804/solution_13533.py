#Start your python function here
def filtra_pares(tupla):
    x = ()
    for i in tupla:
        if (tupla[i]%2==0 or (tupla[i]*-1)%2==0):
            x[i] = tupla[i]
	return x