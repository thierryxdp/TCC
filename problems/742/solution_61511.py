# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Dados o valores em str de s e x, e de i para
    a posição a se concatenada na string, retorna e concatena
    o caracter x na string s; str, str, int -> str"""
    if i=>0 and i<len(s):
        return s[0:i]+x+s[i+1:]