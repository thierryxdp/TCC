def fatorial(n):
	ant=n
    while ant>0:
        n=(ant-1)*n
    ant=ant-1
    return n