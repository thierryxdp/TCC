'''funçao que, fornecida uma string (s), insere o caracter "#"
no inicio, no meio e no final dela
str -> str'''
def hashtag(s):
    media = len(s) //2
    s="#"+s[0:media]+"#"+s[media:]+"#"
    return s