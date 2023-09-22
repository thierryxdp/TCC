def soma_h(N):
	H=0.1
    if N==1:
        return 1
    for n in range(1,N):
        H+=1/n
    return round(H,2)