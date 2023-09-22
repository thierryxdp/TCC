def substitui(s,x,i):
    '''Substitui um texto em um caractere de um outro texto, dada a sua posicao.
	Escreva o texto base (que ira ter o caractere substituido), o texto que sera
    implementado no texto base, e a posicao do caractere do texto base que sera
    substituido. ATENCAO: 1. os textos devem ser escritos dentro de ""; 2. a posicao
    do caractere (i) e dada 0 como primeiro caractere e o ultimo caractere e dado
    pela posicao da ultima letra menos 1.
    
    #paramentros | in: str (texto base), str (texto de subistituicao), i (posicao 
    da letra que sera substituida) -> out: str (texto de saida)'''
	if i>=len(s) or i<0:
		return "valor invalido. Digite um valor de 0 (que representa o primeiro caractere), e o numero total de caracteres da entrada de texto, menos 1 caractere."
	else:
		return s[:i]+x+s[i+1:]