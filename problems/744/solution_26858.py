# Recebe uma string e adiciona uma hastag (#) em seu início, meio e fim
# str-> str
def hashtag(s):
    meio = len(s)//2
    return '#' + s[:meio] + '#' + s[meio:] + '#'