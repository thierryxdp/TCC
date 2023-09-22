def hashtag(s):
    "adiciona uma # no início, meio e final de uma string"
    comprimento = len(s)
    return "#"+s[:comprimento//2] + "#" + s[comprimento//2:]+"#"