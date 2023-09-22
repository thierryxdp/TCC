# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'string, int, int -> string'
    'Substitui o caractere da posicao i da string s pelo caractere x'
    if len(s)>=i:
        return s.replace(s[i],'x')