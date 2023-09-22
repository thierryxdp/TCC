# Recebera uma string e insira o caractere # no inicio,meio e fim
# s
# str-> str
def hashtag(s):
    #x =s[:len(s)//2]
    #y =s[len(s)//2:]
    #s = "#" + x + "#" + y + "#"
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s