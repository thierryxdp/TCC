# Recebe uma string e insere o caractere "#" no início, no meio e no fim dela
# str-> str
def hashtag(s):
    s = '#'+ s[0:3]+ '#'+ s[3:]+ '#'
    return s