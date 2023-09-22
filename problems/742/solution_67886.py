def substitui(s,x,i):
    """funçao que recebe uma string s, um caractere x e umnumero inteiro i entre 0 e o comprimento da string, e retorne uma string igual a s, exceto que o elemento
da posiçao i deve ser substitúıdo pelo caractere x"""
    return s[:i]+str(x)+s[i+1:]