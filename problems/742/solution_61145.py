def substitui(s,x,i):
	'''Esta função recebe uma palavra (s), um caractere (x)
	e um número inteiro (i, entre 0 e comprimento da string)
	e retorna a mesma palavra, exceto que na posição de i 
	terá o caractere x.
	str, str, int -> str'''

    s1=s[:i]
    s2=s[i+1:]
    i=str(i)
    
    return (s1+x+s2)