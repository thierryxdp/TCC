# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if len(s) < i:
        nova_s = s.replace(s[i],'x')
        return nova_s