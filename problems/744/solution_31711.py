# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """recebe uma string s e insere o caractere # em seu início, meio e fim;
str -> str."""
    nome = s[0:(len(s)//2)]
    posnome = s[(len(s)//2):]
    return '#' + nome + '#' + posnome + '#'