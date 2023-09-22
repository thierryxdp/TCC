def fatorial (n):
    '''calcula o fatorial de um número; entrada é o n;
    int->int'''
    f=1
	while (n > 0):
        f= f* n
        n= n -1
       	
	return f