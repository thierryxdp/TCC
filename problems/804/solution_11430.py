#Start your python function here
def filtra_pares(t:tuple)->tuple:
	t2 = ()
	if t[0]%2==0:
		t2=t2+(t[0],)
	if t[1]%2==0:
		t2=t2+(t[1],)
    if t[2]%2==0:
		t2=t2+(t[2],)    
	if t[3]%2==0:
		t2=t2+(t[3],)
	return t2