# Recebe uma string e insere o caractere "#" no início, no meio e no fim dela
# str-> str
def hashtag(s):
    return str('#')+ s[0:]+ str('#')+ s[4:6]+ str('#')