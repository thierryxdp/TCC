# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Retorna a string dada com o caractere '#' no
    inicio, meio e final da string;
    string -> string'''
    meio = len(s) // 2
    return '#' + s[:meio] + '#' + s[meio:] + '#'