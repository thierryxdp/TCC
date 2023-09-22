# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
 """retorna uma string nova com a string X na posição i da string antiga
    str,str,int -> str"""
def substitui(s,x,i):
    if i>0 and i<len(s):
        return s[:i]+x+s[i+1:]