# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' retorna, a partir de uma string s, uma nova string parecida com s, porém com o elemendo da posição i substituido pelo caractere x'''
    letrai=s[i]
    return str.replace(s,letrai,x,-1)