#Start your python function here
def filtra_pares(n1:int,n2:int,n3:int,n4:int)->tuple:
    #essa função faz o filtro de números pares
    t=(n1,n2,n3,n4)
    x=0
    a,b,c,d="","","",""
    if (n1%2==0):
        a=t[0]
    if n2%2==0:
    	b=t[1]
    if (n3%2==0):
    	c=t[2]
    if (n4%2==0):
    	d=t[3]
    t1=(a,b,c,d)
   
	return t1[0]+t1[1]+t1[2]+t1[3]