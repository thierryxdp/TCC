def substitui(s,x,i):
    # substitui uma caractere numa posição especifica por outro/ string,int,int ~> string
    vetor_string = []
    if i > len(s):
    	return 
	else : 
   		s = s[:i] + x + s[i+1:]
    return s