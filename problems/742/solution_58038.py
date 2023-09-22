# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna uma string s com o elemento de posoção i trocado por caractere x; str, str, int -> str'''
    string = s
    string[i] = x
    return string