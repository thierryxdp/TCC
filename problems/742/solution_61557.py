def substitui(s,x,i):
    '''Função que retorna a substituição de uma dada posição na string por uma letra x escolhida.
    Parâmetros: str,str,int -> str'''
    return s[0:i] + x + s[i+1:]