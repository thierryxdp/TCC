def uppCons(frase):
    '''Função que recebe uma frase como entrada e retornará a mesma frase, apenas com as consoantes em maiúsculas. str -> str'''
    i=0
    f=frase
    while i<len(f):        
        if f[i] in ('BCDFGJKLMNPQRSTVWXZ') or ('bcdfgjklmnpqrstvwxz') and f[i]==f[0]:
            g=f[i+1:]
            c=str.upper(f[i])
            f=c+g            
        elif f[i] in ('BCDFGJKLMNPQRSTVWXZ') or ('bcdfgjklmnpqrstvwxz') and not(f[i]==f[0]) and not(f[i]==f[-1]):  
    		g1=f[:i]
            g2=f[i+1:]
            f=g1+str.upper(f[i])+g2            
    	elif f[i] in ('BCDFGJKLMNPQRSTVWXZ') or ('bcdfgjklmnpqrstvwxz') and f[i]==f[-1]:
    		g1=f[:-1]            
            f=g1+str.upper(f[i]) 
        i=1+i
    return f