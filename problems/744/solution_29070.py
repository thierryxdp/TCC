# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ Função que recebe uma string e insere o caractere # no início, no meio e no final dela;
    str -> str"""
    meio = s[round(len(s)/2,0)]
    inicio = s[ :meio: ]
    fim = s[meio: :]
    return '#' + inicio + '#' + fim + '#'