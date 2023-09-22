#Insere um # no inicio, meio e final da string (s)
# str-> str
import math
def hashtag(s):
    meio = math.floor(len(s)/2)
    return '#' + s[0:meio] + '#' + s[meio:len(s)] + '#'