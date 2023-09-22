# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' essa função retorna a string s, porém com o elemento i substituído por x
    str, int, int -> str'''
    0<=i <= len (s) 
    sx =s[0:i] + str(x) + s[i+1:]
    return sx