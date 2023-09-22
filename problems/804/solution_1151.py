#Start your python function here
def filtra_pares(t):
	par = (t[0] % 2 == 0)

	if par:
        return 1 + par*(t[1:])
    elif:
        return par*(t[1:])