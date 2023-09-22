def pontos_por_time(L):
	i=L[0]
	v=L[1]
    Gi=i[2]
    Gv=v[2] 
    
    if Gi[0]>Gi[1]:
    	P1i=3
    	P2i=0
    elif Gi[0]<Gi[1]:
    	P1i=0
    	P2i=3
    else:
    	P1i=1
    	P2i=1
    if Gv[0]>Gv[1]:
    	P1v=3
    	P2v=0
    elif Gv[0]<Gv[1]:
    	P1v=0
    	P2v=3
    else:
    	P1v=1
    	P2v=1
    
    PF1=P1i+P2v
    PF2=P2i+P1v
	
	PontuacaoTime={i[0]:PF1, i[1]:PF2}
	return PontuacaoTime