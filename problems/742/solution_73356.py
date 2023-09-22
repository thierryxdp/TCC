# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    def substitui(s,x,i):
    n = len(s)
    l = s.find(s[i-1:i])+1
    if l==i:
        return s.replace(s[l-1:l],x)
    else:
        return s