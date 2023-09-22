def substitui(s,x,i):
    '''funcao que calcula a subsituicao de uma string por outra
    	s: str-> str 
        x: str-> str caracter que altera o texto
        i: int-> int posicao na qual x substituira em s
        return:
    '''
    return s[:i] + x + s[i+1:]