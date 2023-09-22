def substitui(s,x,i):
    """dado uma string s, a função substitui o caractere da posição
    i com o caractere x; str,str,int-> str"""
    s= 's'
    return s[0:i] + x + s[i+1: len(s)]