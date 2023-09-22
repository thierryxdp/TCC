# esta função faz a substituição, e retorna uma string igual a s, exeto 
# i<= len(s) or 0>=i
# string, int, int -> string
def substitui(s,x,i):
	if i<= len(s) or 0>=i:
		return s[:i] + str(x)+ s[i+1:]