# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''''funcao recebe string e insere # no inicio e no final''''
    meio = len(s) // 2
    stpl = '#' + s[:meio] + '#' + s[meio:] + '#'
    return stpl