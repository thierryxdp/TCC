def uppCons(frase):
    """ A função receberá uma frase como entrada e deve
    retornar a frase com todas as consoantes da mesma em
    maiúscula (os demais caracteres permanecem como estavam
    na frase original).
    
    Entrada: String
    Saída: String"""
    
    consoante='b,c,d,e,f,g,h,i,j,k,l,m,n,p,q,r,s,t,v,x,w,y,z'
    c_maiuscula=''
    while frase in consoante:
        if frase in consoante:
            c_maiscula=c_maiuscula+consoante.upper()
     
    return frase