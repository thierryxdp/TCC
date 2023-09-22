def lingua_p(palavra):
    """
    	Retorn a palavra inserida na língua do P
        str -> str
    """
    palavra_P=palavra
    for i in range(len(palavra)):
        if palavra[i] in 'AaEeIiOoUu':
            palavra_P=palavra_P[0:i]+(str(palavra_P[i])+'p'+str(palavra_P[i])+palavra_P[i+1:]
  	return palavra_P