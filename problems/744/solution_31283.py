''' dado uma string s retorna hastag no inicio, no meio e no fim da string
str -> str'''
def hashtag(s):
    return s[:0]+"#"+s[1:(len(s)/2)]+"#"+s[(len(s)/2):]+"#"