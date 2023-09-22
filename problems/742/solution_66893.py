def substitui(s,x,i):
   '''funçao que recebe uma string e modifica o elemento de posiçao i por um caractere x. str->str'''
	return s[ :i]+ x + s[i+1:]