def substitui(s,x,i):
    """funcao que recebe uma string s, um caractere x no formato
    string e um inteiro i entre 0 e comprimento da string e retorna
    uma string parecida com s porem com o caractere x no lugar
    do elemento de posicao i
    str, str, int -> str"""
    return s[0:i] + x + s[(i+1):]