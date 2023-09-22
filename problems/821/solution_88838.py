def fatorial(n):
    """
    	calcúla o fatorial de dado número n
    	int -> int
    """
    i=1
    if n==0:
        fat=1
    else:
        fat=n
    while (n-i)>0:
        fat = fat*(n-i)
        i+=1
    return fat