# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    tamanho=len(s)
    print(tamanho)
    return '#'+s[0:tamanho/2]+'#'+s[tamanho/2:]+'#'