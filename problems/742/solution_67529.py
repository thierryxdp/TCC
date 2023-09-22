def substitui(s,x,i):
    """A função recebe uma string s, um caractere x e um número inteiro i
entre 0 e o comprimento da string e retorna s, exceto que o elemento da posição
i da string foi substituído por x"""
    if 0 < i < len(s):
        x = str(x)
        return s[0:i]+x+s[i+1:]