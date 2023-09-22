# Calcular uma função que recebe uma string e 
#retorna com # no inicio, meio e fim da funçao
# str-> str
def hashtag(s):
    antes = s[:len(s)//2]
    depois = s[len(s)//2:]
    tag = '#' + antes + '#' + depois + '#'
    return tag