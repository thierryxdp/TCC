def filtra_pares(t):
    if t[0]%2==0:
    	t[0]=str(t[0])+","
    else:
        t[0]=""
    if t[1]%2==0:
    	t[1]=" "+str(t[1])++","
    else:
        t[1]=""
    if t[2]%2==0:
    	t[2]=" "++str(t[2])+","
    else:
        t[2]=""
    if t[3]%2==0:
    	t[3]=" "+str(t[3])
    else:
        t[3]=""
    return "("+str(t[0])+str(t[1])+str(t[2])+str(t[3])+")"