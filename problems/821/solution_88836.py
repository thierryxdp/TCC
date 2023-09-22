def fatorial(n):
    """
    	calcúla o fatorial de dado número n
    	int -> int
    """
    i=1
    num=n
    while (n-i)>0:
        num = num*(n-i)
        i+=1
    return fat