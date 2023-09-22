#Start your python function here
def filtra_pares(t):
    w=int(t[0:2])
    x=int(t[3:4])
    y=int(t[5:6])
    z=int(t[7:])
	return filter(t %2 == 0)