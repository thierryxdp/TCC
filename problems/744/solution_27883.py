# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    meio = len(s)/2
    meio = int(meio)
    comeco = s[:meio]
    final = s[meio:]
    return '#'+comeco+'#'+final+'#'