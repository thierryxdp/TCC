"""obtemos o valor da string e inserimos no inicio meio e fim dela "#"""""
# str-> str
def hashtag(s):
    a= len(s)//2
    return str("#")+s[0:a]+str("#")+s[a:]+str("#")