# Insere hashtag no inicio, meio e final de uma string
# str-> str
def hashtag(s):
    comeco = '#' + s[0]
    i = (s//2)
    meio = '#'+ s[i]
    final = s[-1]+'#'
    
    return str(comeco+meio+final)