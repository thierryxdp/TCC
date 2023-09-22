def substitui(s,x,i):
	'''
recebe uma str 's', um caractere 'x' e u numero inteiro
'x' e retorna a mesma str 's', mas com o caractere 'x'
no lugar do caractere que estava na posicao i 
dados de entrada: str, str, int
retorna: str
	'''
    return s[0:i] + x + s[i+1:]