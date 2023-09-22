def substitui(s,x,i):
    """Função que, ao receber uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string, retorna uma string igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x
    str,str,int->str"""
    return s[0:i]+str(x)+s[i+1:]