#Start your python function here

def filtragem_pares(tupla):
    a,b,c,d=tupla
    tupla1=()
    if a%2==0:
    	 tupla1=tupla1+(a,)
    elif b%2==0:
       	tupla1=tupla1+(b,)
    elif c%2==0:
    	 tupla1=tupla1+(c,)
    elif d%2==0:
    	 tupla1=tupla1+(d,)
    return tupla1