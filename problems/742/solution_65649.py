def substitui(s,x,i):
    """Funcao que ao receber uma string s, um caractere x e um numero inteiro i, retorna a string alterada o i pelo x, sendo a posiçao do caractere substituido: str, float, int=> str"""
    return s[0:i] + x + s[i + 1:]