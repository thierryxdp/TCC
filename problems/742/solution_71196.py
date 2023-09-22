def substitui(s,x,i):
    '''Função que retorna uma string igual à string de entrada s, exceto que seu elemento de posição i foi substituído pelo caractere x;
    entrada: str, int, int;
    saída: str
    '''
    return s[:i] + str(x) + s[i+1:]