# Função que adiciona uma hashtag no inicio, meio e fim da String
# str-> str
def hashtag(s):
    x = len(s)//2
    new_s = "#" + s[:x] + "#" + s[x:] + "#"
    return new_s