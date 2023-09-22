# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    x = len(s)//2 
    return '#' + str(s)[0] + '#' + str(s)[x] + '#' + str(s)[: + 1] + '#'