# Insere hashtag no inicio, meio e final de uma string
# str-> str
def hashtag(s):
    l = list(s)
    l[:-1:2] = '#'
    a = "".join[l]
    return str(a)