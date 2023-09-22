# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    Char_inicio = s[:i]
    Char_fim = s[i+1:]
    Char_compt = Char_inicio + x + Char_fim
    return Char_compt