# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Retorna uma string com # no começo, meio e fim.
    Testes: hashtag('ab') == '#a#b#'
    hashtag('abc') == '#a#bc#'
    Assinatura: str --> str
    """
    meio = int(len(s)/2)
    return '#' + s[0:meio] + '#' + s[meio:len(s)] + '#'