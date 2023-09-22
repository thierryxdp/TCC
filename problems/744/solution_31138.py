# Insere hashtag no inicio, meio e final de uma string
# str-> str
def hashtag(s):
    comeco = s[0]
    meio = s[s//2]
    final = s[-1]
    return str(meio)