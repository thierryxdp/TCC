""" função que fornece a posição de uma letra desejada em uma frase segundo a ocorrencia desejada
str,str,int -> int""""
def posLetra(s,l,n):
    o=0
    for i in range(len(s)):
    	if s[i]==l:
        	o=o+1
        if o==n:
            return i
    return-1