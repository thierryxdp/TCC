def substitui(s,x,i):
    """Essa função substitui um caracter que se encontra na posição
    i (que deve estar contido entre 0 e comprimento da string) por 
    um caracter x de uma string s. Como entrada temos uma string(S),
    um caracter(x) e um número inteiro (i), e como saída temos sua 
    substituição;
    str,int,int,-> str"""
    s_nova= s.replace(s[:i],x)
    return s_nova