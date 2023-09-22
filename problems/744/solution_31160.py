# Insere hashtag no inicio, meio e final de uma string
# str-> str
def hashtag(s):
    meio = s[:2]
    return '#' + str(meio) + s + '#'