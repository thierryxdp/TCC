# Recebe uma string e insere o caractere "#" no ínicio,meio e fim dela.
# str-> str
def hashtag(s):
    inif = '#'
    met = len(s)//2
    return inif + s[0:met] + inif + s[met: ] + inif