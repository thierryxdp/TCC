def substitui(s, x, i):
    '''Função que dado uma string s, um caractere x e um inteiro i, entre 0 e o comprimento da string,
 	retorne a string s com o caractere x substituida na posição i
    str, str, int -> str'''
    StrAntesDeI = s[:i]
    StrDepoisDeI = s[i + 1:]
    return StrAntesDeI + x + StrDepoisDeI