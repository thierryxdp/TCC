#Start your python function here
def filtra_pares(x):
    y = ()
    if (x[0]%2 == 0):
        y = x[0]
	if (x[1]%2 == 0):
        y[1] = x[1]
	if (x[2]%2 == 0):
        y[2] = x[2]
	if (x[3]%2 == 0):
        y[3] = x[3]
	return y[0]+y[1]+y[2]+y[3]