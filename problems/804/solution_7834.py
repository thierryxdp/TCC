#Start your python function here
def filtra_pares(t):
    if t[0]%2 == 0:
        x = t[0]
	if t[1]%2 == 0:
        x = x , t[1]
    if t[2]%2 == 0:
        x = x , tuple(t[2])
    if t[3]%2 == 0:
        x = x , tuple(t[3])
    return x