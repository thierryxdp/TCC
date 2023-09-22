# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """função que retorna uma string com substituição de i por x; str, int, int->string"""
    t=s[0:i]
    t=t+str(x)
    return t+s[i+1:]