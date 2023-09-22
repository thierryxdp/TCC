# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna a string s com o elemento da posiçao i substituído rin
    pelo caracetere x
    string, string, int-> string'''
    frase = s[i:i+1]
    return frase + x