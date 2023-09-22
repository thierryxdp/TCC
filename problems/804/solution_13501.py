#Start your python function here
def filtra_pares(tupla):
    x = ()
    for i in range(0,4):
        if (tupla[i]%2==0 or (tupla[i]*-1)%2==0):
            x + tupla[i]
	return x