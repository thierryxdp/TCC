# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Cálculo de uma função que recebe uma string e insere um caractere "#"
    no início, no meio e no fim desta."""
    return '#' + s[0:len(s)//2] + '#' + s[len(s)//2:] + '#'