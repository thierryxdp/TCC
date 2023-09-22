def substitui(s,x,i):
    # substitui uma caractere numa posição especifica por outro/ string,int,int ~> string
    if i > len(s):
    	return "Posição Escolhida é maior que a palavra"
	else :
        vetor_string = [s]
        vetor_string[i] = x
        return vetor_string