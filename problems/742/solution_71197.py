def substitui(s,x,i):
    '''Função que retorna uma string igual à string de entrada s, exceto que seu elemento de posição i foi substituído pelo caractere x;
    entrada: str, int, int;
    saída: str
    '''
    s1= s[:i] + str(x) + s[i+1:] # variável igual à string após a operação de substituição
    return s1