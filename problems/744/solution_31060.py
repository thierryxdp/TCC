# Recebe uma string e insere o caractere "#" no início, no meio e no fim dela
# str-> str
def hashtag(s):
    #inicio = s[:len(s)//2]
    meio = s[len(s)//2:]
    fim = "#" + inicio + "#" + fim + "#"
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s