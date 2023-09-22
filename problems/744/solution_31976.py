# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que recebe uma string e insere o caractere "#" no início, no meio e no final dela."""
    return str('#' + str(s[0:(int(len(s)//2))] + '#' + str(s[(int(len(s)//2) + 1):] + '#')