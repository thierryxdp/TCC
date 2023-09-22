def substitui(s,x,i):
    """Retorna uma string s exceto com o seu elemento da posição i; str,str,int->str"""
    a = len(s)
    return s[:i] + s[i+1:a]