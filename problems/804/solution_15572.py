def filtra_pares(s):
	X=[]
    if(s[0]%2==0):
    	X[0,]=s[0]
	if(s[1]%2==0):
    	X[1,]=s[1]
	if(s[2]%2==0):
    	X[2,]=s[2]
	if(s[3]%2==0):
    	X[3,]=s[3]
	return X[0],X[1],X[2],X[3]