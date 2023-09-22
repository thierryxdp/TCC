def hashtag(s):
    "adiciona uma # no início, meio e final de uma string"
    comprimento = len(s)
    return "#".join(s[:comprimento//2]) + "#".join(s[comprimento//2:])