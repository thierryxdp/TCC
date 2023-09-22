def primo(numero):
    div=[]
    for c in range(1,numero+1):
        if numero%c==0:
            div=(div+[c])
        	if len(div)==2:
            	return True
        	else: 
            	return False