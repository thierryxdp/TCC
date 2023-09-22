def hashtag(s):
    """A função retorna uma string com # no inicio meio e fim. Basicamente
     é feita de uma forma simples abusando da função len() e da //.
    pre = s[:len(s)//2]
    pos = s[len(s)//2:]
    s = "#" + pre + "#" + pos + "#"
    Depois basta retornar s.
    Assinatura: str ---> str
    testes:
    hashtag('abba')=='#ab#ba#'
    hashtag('s')=='##s#'
    hashtag('Arara')=='#Ar#ara#'
    """
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s