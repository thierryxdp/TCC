#Função substitui posicionamento i para item x
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i>=0 and i<=len(s):
        return s[:i]+x+s[i+1:]