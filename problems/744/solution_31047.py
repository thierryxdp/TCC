# Recebe uma string e insere o caractere "#" no início, no meio e no fim dela
# str-> str
def hashtag(s):
    return '#'+ s[:'#']+ '#'+ len(s)[:6]+ '#