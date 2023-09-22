def qtd_divisores(N):
    s=0
    t=1
    while t<N+1:
        
            if N%t==0:
            	s+=1
            	t+=1
            else:
                t+=1
    return s