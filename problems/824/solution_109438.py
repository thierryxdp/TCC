listaconsoantes = [q,w,r,t,y,p,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m]
def uppCons(F):
    for i in range(len(F)):
        F = [i]
        if F in listaconsoantes:
            F = F.uppercase
	return F