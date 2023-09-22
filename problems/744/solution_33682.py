#Função que receba string e insira # no inicio
# str-> str
def hashtag(s):
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s