# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    if len(s) % 2 > 1:
        meio = round(len(s)/2)
    elif len(s) % 2 < 1:
        meio = round(len(s)/2)+1
    
    nova_frase = '#' + s[:meio] +'#' +s[meio:] + '#'
    return nova_frase