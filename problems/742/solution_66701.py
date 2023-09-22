# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Substitui na string s o elemento de posição i pelo caracter x
    str, str, int->str"""
    if i>len(s):
        return "a posição mencionada não existe na string"
    else
        l=len(s)
        a=(i-1)
        b=(i+1)
        resp=s[0:a]+x+s[a:l]
        return resp