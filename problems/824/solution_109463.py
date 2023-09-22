listaConsoantes = []
consoantes = q,w,r,t,y,p,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m

def uppCons(frase):
    for i in range(len(frase)):
        frase = [i]
        if frase in listaConsoantes:
            frase = frase.uppercase
	return frase