''' dado uma string s retorna hastag no inicio, no meio e no fim da string
str -> str'''
def hashtag(s):
    i=len(s)//2
    
    return s[:1]+"#"+s[1:i]+"#"+s[i:]+"#"