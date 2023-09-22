# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função substitui na string s de entrada o caractere na
    posição i pelo caractere x. str,int,int->str"""
    s1= i+1
    nova_s= s[:i]+x+s[s1:]
    return nova_s