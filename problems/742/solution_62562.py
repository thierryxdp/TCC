def substitui(s,x,i):
    '''
    Funcao que recebe uma string s, um caratere x e um inteiro i entre 0 e o comprimento da string s, e retorna uma string igual a s,
	exceto que o elemento da posicao i deve ser substituido pelo caratere x.
    Parâmetros:
    	s: str
        x: str
        i: int
    Saída:
    	str
    '''
    return s[0:i] + x + s[i+1:len(s)]