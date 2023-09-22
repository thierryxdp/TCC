# Recebe uma string e insere o caractere "#" no início, no meio e no fim dela
# str-> str
def hashtag(s):
    s = '#'+ s[:len(s) // 2]+ '#'+ s[len:(s) //2]+ '#'