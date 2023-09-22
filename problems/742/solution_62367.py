def substitui(s,x,i):
    '''
   	Função que retorna uma string igual a s, exceto que o elemento
da posição i deve ser substituído pelo caractere x,dada a tupla(s,x,i);
tupla -> string
	'''
    return s[:i]+x+s[i+1:]