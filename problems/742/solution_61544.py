# Função que substitui um caractere escolhido por outro da string escohida
# de acordo com a posição do caractere original da string.
# str,str,int -> str
def substitui(s,x,i):
    return  s[0:i] + x + s[i + 1:]