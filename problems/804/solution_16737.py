def filtra_pares(s):

    if (s[0])/2==int((s[0])/2):
    	filtrado1=(s[0],)
    else:
        filtrado1=()
    if s[1]/2==int(s[1]/2):
		filtrado2=(filtrado1,s[1])
	else:
        filtrado2=filtrado1
    if s[2]/2==int(s[2]/2):
		filtrado3=(filtrado2,(s[2]))
	else:
        filtrado3=filtrado2
    if s[3]/2==int(s[3]/2):
		filtrado4=(filtrado,s[3])
	else:
        filtrado4=filtrado3
    return(filtrado4)