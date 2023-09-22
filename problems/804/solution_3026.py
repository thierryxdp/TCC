#Start your python function here

def filtra_pares(tupla):
    a,b,c,d=tupla
    tupla1=()
    if a%2==0:
    	 tupla1=tupla1+(a,)
    if b%2==0:
       	tupla1=tupla1+(b,)
    if c%2==0:
    	 tupla1=tupla1+(c,)
    if d%2==0:
    	 tupla1=tupla1+(d,)
    return tupla1