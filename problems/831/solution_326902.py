def lingua_p(palavra):
    """Esta função recebe uma palavra e traduz ela para a língua do P
    str -> str"""
	palavra_p=''
	i=0
	while i < len(palavra):
    	if palavra[i]==' ':
        	palavra_p += ' '
    	else:
        	i = i+1
        	palavra_p = palavra_p + codigo[i]
    	i=i+1
	return palavra_p