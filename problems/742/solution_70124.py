def substitui(s,x,i):
  	"""substitui em s um caracter x na posição i,substitui(s,x,i)"""
	# 0<i<len(s)
    return s[0:i]+str(x)+s[i+1:len(s)]