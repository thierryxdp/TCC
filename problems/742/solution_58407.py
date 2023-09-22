def substitui(s,x,i):
    """Esta função recebe como entrada 3 argumentos e retorna uma string igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x, str,str,int->str"""
    if i>=0 and i<=len(s):
        return s[:i]+str(x)+s[i+1:]