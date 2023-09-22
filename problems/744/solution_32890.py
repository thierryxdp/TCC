# Escolha nomes elucidativos para suas variáveis
def hashtag(s):
    """ Retorna a string com o caractere "3" no inicio no meio e no final
    str -> str"""
    antes = s[:len(s)//2]
    depois = s[len(s)//2:]
    s = "#" + antes + "#" + depois + "#"
    return s