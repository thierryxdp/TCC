def substitui(s, x, i):
    """função que recebe uma string(s), uma caractere(x) e um numero inteiro(i) entre 0 0 e o comprimento da string, e retorna uma string igual a s"""
    nova_string=s[0:i-1]+ x +s[i:]  
    return nova_string