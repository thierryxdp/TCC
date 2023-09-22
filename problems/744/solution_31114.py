# Função que insera uma # no início, no meio e no final da string
# s é uma tring qualquer
# str-> str
def hashtag(s):
    return "#"+s[0:(len(s)/2)]+"#"+[(len(s)/2):]+"#"