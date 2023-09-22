def substitui(s, x, i):
    """função que recebe uma string(s), uma caractere(x) e um numero inteiro(i) entre 0 0 e o comprimento da string, e retorna uma string igual a s"""
    nova_string=s[0:i-1]+ x +s[i:]  
    #adiciona os elementos de s(da posição inicial 0 até a anterior a i) na variavel nova_string, adiciona o caracter x e depois adiciona o resto dos elementos de s.
    return nova_string