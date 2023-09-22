def posLetra(s,a,n):
    ''' retorna em que posição da string aquela ocorrência da letra(1 para primeira ocorrência, 2 para segunda, etc) está, dada uma string s, uma letra a e um número n;
    str,str,int -> int '''
	i = 0
    while i<=len(s):
        if a in s:
            if n>=i:
            	return str.index(s,a,n)
            if n<i:
                return -1
        else:
            return -1
    i = i + 1