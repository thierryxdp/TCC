# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str

def hashtag(s):
    primeiroIndice = len(s // 2)
    palavraNova = '#' + s[ : primeiroIndice] + '#' + s[primeiroIndice + 1: ] + '#'
    return palavraNova