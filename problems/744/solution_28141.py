# Função que recebe uma string e retorna # no ínicio no meio e no final.
# str-> str
def hashtag(s):
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s