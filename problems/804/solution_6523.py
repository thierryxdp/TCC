def filtra_pares(e):
    
    resposta=()
	
    if (e[0]%2==0):
		resposta=resposta+(e[0],)
	if (e[1]%2==0):
		resposta=resposta+(e[1],)
	if (e[2]%2==0):
		resposta=resposta+(e[2],)
	if (e[3]%2==0):
		resposta=resposta+(e[3],)
	else:
   		return resposta