def substitui(s,x,i):
    """Recebe uma string s, um caractere x e um número inteiro i entre 0 e o comprimento da string e retorna uma string igual a s, exceto que o elemento da posição i deve ser substituido pelo caractere x; str, str, int-> str"""
    return str(s[0:i])+str(x)+str(s[i:])