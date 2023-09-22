# Recebe uma string e insere o caractere "#" no início, no meio e no fim dela
# str-> str
def hashtag(s):
    s = '#'+ s[0:2]+ '#'+ s[2:5]+ '#'
    return s