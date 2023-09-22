#Start your python function here
def filtra_pares(k):
    t=()
    if k[0]%2 == 0:
        t=(t + k[0],)
    if k[1]%2 == 0:
        t=(t + k[1],)
    if k[2]%2 == 0:
      	t=(t + k[2],)
    if k[3]%2 == 0:
    	t=(t + k[3],)
    return t