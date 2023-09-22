''' dado uma string s retorna hastag no inicio, no meio e no fim da string
str -> str'''
def hashtag(s):
    i=len(s)//2
    
    return s[:0]+"#"+s[0:i]+"#"+s[i:]+"#"