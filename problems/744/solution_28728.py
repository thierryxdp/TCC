# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(string):
    qntd_letras=len(string)
    metade=qntd_letras//2
    inicio=string[:metade]
    meio=[metade-1:metade+1]
    fim=string[metade:]
    return '#'+inicio+'#'+meio+fim+'#'