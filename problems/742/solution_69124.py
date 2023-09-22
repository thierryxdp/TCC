# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Função que recebe uma string (s), um caractere (x), um número inteiro (i) 
        e substitui um caractere de uma string por outra string """
    return s[:i] + x + s[i+1:]