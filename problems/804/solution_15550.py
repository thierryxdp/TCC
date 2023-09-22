def filtra_pares(s):
    t1=s[0]
    t2=s[1]
    t3=s[2]
    t4=s[3]
    if (((t1%2==0)and(t2%2==0))and((t3%2==0)and(t4%2==0))):
    	return s
    else if (not((t1%2==0)and(t2%2==0))and((t3%2==0)and(t4%2==0))):
        return ()+s[1]+s[2]+s[3]
    else if