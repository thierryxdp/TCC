# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    meio = len(s)/2
    meio = int(round(meio))
    M = "#" + s[:meio] + "#" + s[meio:] + "#"
    return M