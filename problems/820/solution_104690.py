def posLetra(s,a,n):
    '''Função que retorna em que posição da string aquela ocorrencia da letra está, dada uma string
    str,str,int -> int'''
	i = 0
    x = ''
    while i<=len(s):
        if a in s:
            if n>str.count(s,a):
                return -1
            else:
                return str.find(s,a,n-1)
   		i = i + 1