def substitui(s,x,i):
    """Calcula e retorna uma string igual a s, alterando apenas o elemento da posição i pelo caracter x
    Entradas: string(s), caracter(x) e posição(i)
    string,float,int-->string"""
    y = str(s[:i])
    g = str(s[i+1:])
    return str(y)+str(x)+str(g)