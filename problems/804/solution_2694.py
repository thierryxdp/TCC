#retorna uma tupla contendo apenas os elementos pares da tupla de entrada
#entrada deve ser uma tupla contendo 4 elementos inteiros
#tupla->tupla
def filtra_pares(a,b,c,d):
	if (a%2==0)and(b%2)==0 and(c%2)==0 and(d%2)==0:
		return (a,b,c,d)
	elif(b%2)==0 and (c%2)==0 and (d%2)==0:
		return (b,c,d)
	elif(c%2)==0 and (d%2)==0:
		return (c,d)
	elif (a%2)==0 and (c%2)==0 and (d%2)==0:
            return (a,c,d)
        elif (a%2)==0 and (b%2)==0 and (c%2)==0:
            return (a,b,c)
        elif (a%2)==0 and (b%2)==0 and (d%2)==0:
            return (a,b,d)
        elif(a%2)==0 and (b%2)==0:
            return(a,b)
        elif(a%2)==0 and (c%2)==0:
            return(a,c)
        elif(a%2)==0 and(d%2)==0:
            return(a,d)
        elif(b%2)==0 and(c%2)==0
            return(b,c)
        elif(b%2)==0 and(d%2)==0
            return (b,d)
        else:
            return não há elementos pares