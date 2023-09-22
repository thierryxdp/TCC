# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Retorna a string dada alterada, mudando o 
    elemento da posicao (i) pelo caractere 'x';
    string, string, int -> str'''
    return s[:i] + x + s[i+1:]