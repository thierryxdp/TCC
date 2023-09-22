"""
Nesta função, o que fizemos foi criar duas variáveis que
irão servir como o "começo até i" e "letra pós i" da
string inserida em s, e no meio delas iremos adicionar
o x. O mais importante foi como escolher até que ponto
essas novas variáveis chegam. Também foi adicionado no
código que i <= len(s)
string, int, int -> string
"""
def substitui(s,x,i):
    i <= len(s)
    subs_x = s[0:i]
    continu = s[i+1:len(s)]
    return str(subs_x)+str(x)+str(continu)