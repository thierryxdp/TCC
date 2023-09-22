def uppCons(frase):
    '''Função que recebe uma frase como entrada e retornará a mesma frase, apenas com as consoantes em maiúsculas. str -> str'''
    i=0
    f=frase
    while i<len(f):
        if f[i] in ('AEIOUaeiou'):
            i=i+1                
        if f[i] in ('BCDFGJKLMNPQRSTVWXZ') or ('bcdfgjklmnpqrstvwxz') and f[i]==f[0]:
            g=f[i+1:]
            c=str.upper(f[i])
            f=c+g
            i=i+1
        if f[i] in ('BCDFGJKLMNPQRSTVWXZ') or ('bcdfgjklmnpqrstvwxz') and not(f[i]==f[0]) and not(f[i]==f[-1]):  
    		g1=f[:i]
            g2=f[i+1:]
            c=str.upper(f[i])
            f=g1+c+g2
            i=i+1
    	if f[i] in ('BCDFGJKLMNPQRSTVWXZ') or ('bcdfgjklmnpqrstvwxz') and f[i]==f[-1]:
    		g1=f[:-1]
            c=str.upper(f[i])
            f=g1+c
            i=i+1
    return f