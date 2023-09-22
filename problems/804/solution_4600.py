#Start your python function here
#esta função recebe quatro valores inteiros e devolve os que forem pares 
#int,int,int,int ->int,int,int,int
def filtra_pares(a,b,c,d):
    pares = []
    if a %2 ==0:
    	pares.append(a)
    if b %2 ==0:
       	pares.append(b)
    if c %2 ==0:
        pares.append(c)
    if d %2 ==0:
        pares.append(d)
    return (pares)