def substitui (s,x,i):
    """retorna uma string s de entrada com a substituicao do
    elemento da posicao i de entrada pelo argumento x de
    entrada"""
    return s.replace(s[i:-1],x)