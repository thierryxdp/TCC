def hashtag(s):
    """Retorna uma string com # no começo, meio e fim.
    Testes: hashtag('ab') == '#a#b#'
    hashtag('abc') == '#a#bc#'
    Assinatura: str --> str
    """
    meio = int(len(s)/2)
    return '#' + s[0:meio] + '#' + s[meio:len(s)] + '#'