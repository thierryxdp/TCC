def substitui(s,x,i):
    ''' Função que retorna uma string com a substituição de determinado 
    elemento dela dados uma string (s), um caractere (x) qualquer e a 
    posição do elemento a ser substituido (i) que deve ser entre 0 e o
    comprimento da string
    Entrada: str, str, int
    Retorno: str '''
    
    nova_string = s[:i]+x+s[i+1:]
    
    return nova_string