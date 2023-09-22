# Insere hashtag no inicio, meio e final de uma string
# str-> str
def hashtag(s):
    comeco = '#' + s[0]
    meio = s
    final = s[-1]+'#'
    
    return str(comeco)