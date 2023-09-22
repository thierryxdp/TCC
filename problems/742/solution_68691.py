''' Esta função substitui i pelo caracter x'''
def substitui(s,x,i):
	if i >= len(s) or 0 <= i:
		return s[:i] + str(x) + s[i+1:]
	else:
		return 'não é possivel fazer a substituição'