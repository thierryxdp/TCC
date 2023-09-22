def substitui(s,x,i):
    '''
    recebe uma string 's', um caractere 'x' e um inteiro 'i' entre 0 e o comprimento da string, e retorna uma string igual  a 's', substituindo o 'i' pelo 'x';
    str, int, int -> str
    '''
	s = s[:i] + x + s[i+1:]
    return str(a)