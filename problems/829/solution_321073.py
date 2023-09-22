def soma_h(N):
    def inverso(N):
		return(1/N)
    soma=sum(map(inverso,range(1,N+1)))
	return(round(soma,2))