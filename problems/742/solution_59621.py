# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna ao usuário a string digitada com a modificação de um caractere na posição digitada pelo usuário.
    String, String, Int -> String'''
    novaString= s[:i]+x+s[i+1:]