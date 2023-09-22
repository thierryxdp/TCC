# Coloque um comentário dizendo o que a função faz

# str-> str
def hashtag(s):
    #x= s[:len(s)//2]
    #y = s[len(s)//2:]
    #s = "#" + x + "#" + y + "#"
    s = "#" + s[:len(str1)//2] + "#" + s[len(str1)//2:] + "#"
    return s