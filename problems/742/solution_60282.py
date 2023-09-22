# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """calcula e retorna a string s, em que o seu indice i é substituido pelo caracter x;
    str, int, int -> str"""
    j = i+1
    if 0<=i<len(s):
        return str(s[:i]) + str(x) + str(s[j:])
    else:
        return False