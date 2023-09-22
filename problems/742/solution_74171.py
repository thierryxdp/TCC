# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    if i >= 0 and i <= len(s):
      	s1,s2 = str.partition(s,s[i])
        s = s1 + x + s2
        return s