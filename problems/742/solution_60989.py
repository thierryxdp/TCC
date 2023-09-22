# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funcao que substitui o caractere de s na posicao i pelo caractere x; str,str,int->str"""
    if 0<=i<=int(len(s)):
        return s[:i]+x+s[(i+1):]