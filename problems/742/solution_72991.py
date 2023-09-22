# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna uma string nova com a string X na posição i da string antiga
    str,str,int -> str"""
    if i>0 and i<(s):
        return s[:i]+x+s[i+1:]
    else:
        return "erro"