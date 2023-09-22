#Start your python function here
#tuple->tuple
def filtra_pares(a,b,c,d):
    """Função que retorna uma tupla contendo somente os elementos pares dentre
    os quatro inseridos, na ordem em que são apresentados"""
    if a%2==0:
    	l=a
    elif b%2==0:
    	m=b
    elif c%2==0:
    	n=c
    elif d%2==0:
    	o=d
	return((l,m,n,o))