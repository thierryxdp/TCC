"Insere o caractere # no inicio, meio e final de qualquer string"
"s= string, x= variavel para simplificar"
"str-> str"
def hashtag(s):
    x= int(len(s)/2)
    return "#"+s[:x]+ "#"+ s[x:]+ "#"