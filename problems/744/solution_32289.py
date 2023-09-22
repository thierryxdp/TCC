#Insere um # no inicio, meio e final da string (s)
# str-> str
def hashtag(s):
    meio = round(len(s)/2)
    return '#' + s[0:meio] + '#' + s[meio+1:len(s)] + '#'