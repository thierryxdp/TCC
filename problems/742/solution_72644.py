# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
     """Funçâo que retorna uma dada string s com o caracter da posição i substituído por x
    str,str,int-> str"""
    if 0<=i<=len(s):
        return s[:i]+x+s[i+1:]