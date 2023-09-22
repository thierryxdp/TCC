#Start your python function here
def filtra_pares(t1):
    if (t1[0]%2) ==0:
    	return t1[0]
    elif (t1[1]%2) ==0:
    	return t1[1]
    elif (t1[2]%2) ==0:
    	return t1[2]
    elif (t1[3]%2) ==0:
    	return t1[3]
    return t1[::1]